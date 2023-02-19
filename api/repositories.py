import requests, os
from api.helper_service import ApiSource, HelperService
from base.models import NewsArticle, User, UserLikedNews
import datetime
import pytz

class NewsArticleRepository:
    '''
    This is a News Article Repository that basically brings News Article data either
    from Database or from External APIs. This serves as a good abstraction and decoupled code
    from views.py 
    '''
    expiry_limit = datetime.timedelta(minutes=15)   # 5 minutes expiry limit
    
    def getNewsArticles(self, query: str = None):
        '''
        This methoid decides whether to fetch articles from external APIs or from database.
        This returns a list of NewsArticle Objects.
        '''
        
        # return news articles from database or from external apis
        now = datetime.datetime.now(tz=pytz.timezone('UTC')) - self.expiry_limit
        new_search = False   # flag to indicate if a new search is being made or not
        
        if NewsArticle.objects.all().exists():
            if query is None:
                last_fetched_article = NewsArticle.objects.latest('fetched_at')
            else:
                try:
                    last_fetched_article = NewsArticle.objects.filter(headline__icontains=query).latest('fetched_at')
                except NewsArticle.DoesNotExist:
                    new_search = True

        # if last article was added more than the expiry limit ago, add new articles from external apis
        # or fetch articles if there are no articles in the database
        if (new_search) or (not NewsArticle.objects.all().exists()) or (last_fetched_article.fetched_at < now):
            # update articles from external apis
            self.__addArticlesFromExternalApis(query)
            
        # get articles from database
        articles = self.__getArticlesFromDatabase(query)
        return articles
        
    
    def __getArticlesFromDatabase(self, query: str = None):
        '''
        This method returns news articles from the database ordered by published_at
        '''
        if query is None:
            # Updating fetched_at for all articles
            NewsArticle.objects.all().update(fetched_at=datetime.datetime.now(tz=pytz.timezone('UTC')))
            return NewsArticle.objects.all().order_by('published_at')

        # Updating fetched_at for all articles with the query
        NewsArticle.objects.all().filter(headline__icontains=query).update(fetched_at=datetime.datetime.now(tz=pytz.timezone('UTC')))
        return NewsArticle.objects.all().filter(headline__icontains=query).order_by('published_at')
    
    def __addArticlesFromExternalApis(self, query: str = None):
        '''
        This method gets news articles from external apis and saves them to the database
        '''
        self.__addArticlesFromNewsApiToDatabase(query=query)
        self.__addArticlesFromRedditToDatabase(query=query)
    
    
    def __addArticlesFromRedditToDatabase(self, query: str = None):
        '''
        This method hit the Reddit API and store top 10 articles in the database.
        '''
        api_url = os.getenv('REDDIT_API_URL')
        if query:
            api_url += f'&q={query}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # raises an exception if status code indicates an error
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error occurred: {error}")
            # handle the error, possibly by logging or notifying someone
        except requests.exceptions.RequestException as error:
            print(f"An error occurred: {error}")
            # handle the error, possibly by logging or notifying someone
        else:
            # if no exception was raised, process the response
            data = response.json()
            # getting only top 10 articles from the api
            for items in data["data"][:10]:
                news_article = NewsArticle.objects.filter(headline=items['title'], link=items['url']).first()
                # if news article does not exist in database, add it
                if not news_article:
                    news_article = NewsArticle(
                        headline=items['title'], 
                        link=items['url'], 
                        source='reddit',
                        published_at=HelperService.convertDateTimeStringToDatetime(items['utc_datetime_str'], ApiSource.REDDIT),
                        fetched_at=datetime.datetime.now(tz=pytz.timezone('UTC'))
                    )
                    news_article.save() 
                    
        
    def __addArticlesFromNewsApiToDatabase(self, query: str = None):
        '''
        This method hits News API and stores top 10 News Article in the database.
        '''
        # getting env variables from .env file
        api_key = os.getenv('NEWSAPI_KEY')
        if query:
            api_url = os.getenv('NEWS_API_URL')
            api_url += f'?q={query}&apiKey={api_key}&sortBy=popularity'
        else:
            api_url = os.getenv('NEWS_API_HEADLINES_URL')
            api_url += f'&apiKey={api_key}&sortBy=popularity'
            
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # raises an exception if status code indicates an error
        except requests.exceptions.HTTPError as error:
            print(f"HTTP error occurred: {error}")
            # handle the error, possibly by logging or notifying someone
        except requests.exceptions.RequestException as error:
            print(f"An error occurred: {error}")
            # handle the error, possibly by logging or notifying someone
        else:
            # if no exception was raised, process the response
            data = response.json()
            # getting only top 10 articles from the api
            for items in data["articles"][:10]:
                news_article = NewsArticle.objects.filter(headline=items['title'], link=items['url']).first()
                # if news article does not exist in database, add it
                if not news_article:
                    news_article = NewsArticle(
                        headline=items['title'],
                        link=items['url'], 
                        source='newsapi',
                        published_at=HelperService.convertDateTimeStringToDatetime(items['publishedAt'], ApiSource.NEWSAPI),
                        fetched_at=datetime.datetime.now(tz=pytz.timezone('UTC'))
                    )
                    news_article.save()
    
    
    
class UserRepository:
    '''
    This is a User Repository. It's for managing all data related to Use.
    '''
    
    def getUserFavouriteArticles(self, user_name):
        '''
        This method returns a user's favourite articles
        '''
        if not User.objects.filter(name=user_name).exists():
            return None
        user = User.objects.get(name=user_name)
        return UserLikedNews.objects.all().filter(user=user, favorite=True)
    
    def toggleArticleToFavourites(self, user_name, article_id):
        '''
        This method adds or removes an article to a user's favourites depending on whether 
        the article is already in the user's favourites
        '''
        user: User = None
        news_article: NewsArticle = None
        
        if not NewsArticle.objects.filter(article_id=article_id).exists():
            return False
        
        if not User.objects.filter(name=user_name).exists():
            user = User(name=user_name)
            user.save()
        else:
            user = User.objects.get(name=user_name)

        news_article = NewsArticle.objects.get(article_id=article_id)
        
        if UserLikedNews.objects.filter(user=user, news_article=news_article).exists():
            userLiked = UserLikedNews.objects.get(user=user, news_article=news_article)
            userLiked.favorite = not userLiked.favorite
            userLiked.save()
            return userLiked

        userLiked = UserLikedNews(user=user, news_article=news_article, favorite=True)
        userLiked.save()
        return userLiked
        
            
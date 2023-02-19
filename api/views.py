from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.repositories import NewsArticleRepository, UserRepository
from api.serializers import NewsArticleSerializer, UserLikedNewsSerializerGet, UserLikedNewsSerializerPost


@api_view(['GET'])
def news(request):
    '''
    This is a news endpoint that deals with only GET requests. It returns News Articles either
    from database or External APIs depending on the expiry limit. It also accepts one query parameter
    for searching.
    '''
    try:
        query = request.GET.get('query')
        news_articles = NewsArticleRepository().getNewsArticles(query=query)
        serializer = NewsArticleSerializer(news_articles, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({"error": "Something went wrong"})


@api_view(['GET', 'POST'])
def favourite(request):
    '''
    This is a new/favourite/ endpoint that allows users to favourite articles or get their favourite articles.
    This can also be used for removing any particular favourite article using article ID.
    '''
    userRepo = UserRepository()
    _user = request.GET.get('user')
    if request.method == 'POST':
        try:
            _id = request.GET.get('id')
            if _user and _id:
                userLikedNews = userRepo.toggleArticleToFavourites(_user, _id)
            if userLikedNews:
                serializer = UserLikedNewsSerializerPost(userLikedNews)
                return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)})
    
    try:
        userLikedNews = userRepo.getUserFavouriteArticles(_user)
        serializer = UserLikedNewsSerializerGet(userLikedNews, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response({"error": "Something went wrong"})
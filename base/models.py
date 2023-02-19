from django.db import models

# Create your models here.
class User(models.Model):
    '''
    This is the User model. It Stores basic use info.
    '''
    user_id = models.AutoField(primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"({self.user_id}) {self.name}"
    
    
class NewsArticle(models.Model):
    '''
    This is the NewsArticle model. It stores News Article details.
    '''
    class SourceTypes(models.TextChoices):
        '''
        This is a class for the source types which serves as enums for sources
        '''
        NEWSAPI = 'newsapi'
        REDDIT = 'reddit'
        
    article_id = models.AutoField(primary_key=True)
    added_at = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=100)
    link = models.URLField()
    source = models.CharField(max_length=30, choices=SourceTypes.choices)
    published_at = models.DateTimeField(default=None, null=True)
    fetched_at = models.DateTimeField(default=None, null=True)
    
    def __str__(self):
        return f"({self.article_id}) {self.headline}"
    
    
class UserLikedNews(models.Model):
    '''
    This is the UserLikedNews model. This stores user's favorite articles.
    '''
    user_liked_news_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_article = models.ForeignKey(NewsArticle, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.user_id} likes {self.news_article.article_id}"
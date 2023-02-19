from rest_framework import serializers
from base.models import User, NewsArticle, UserLikedNews

'''
In this file we have Serializer for different Models. Serializers deals with 
the Database Object and converts them into python objects or API response.
'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name']
    

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['headline', 'link', 'source']
 
        
class UserLikedNewsSerializerPost(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name', read_only=True)
    headline = serializers.CharField(source='news_article.headline', read_only=True)
    link = serializers.CharField(source='news_article.link', read_only=True)
    source = serializers.CharField(source='news_article.source', read_only=True)
    id = serializers.IntegerField(source='news_article.article_id', read_only=True)
    
    class Meta:
        model = UserLikedNews
        fields = ['name', 'favorite', 'headline', 'link', 'source', 'id',]
   
        
class UserLikedNewsSerializerGet(serializers.ModelSerializer):
    headline = serializers.CharField(source='news_article.headline', read_only=True)
    link = serializers.CharField(source='news_article.link', read_only=True)
    source = serializers.CharField(source='news_article.source', read_only=True)
    id = serializers.IntegerField(source='news_article.article_id', read_only=True)
    
    class Meta:
        model = UserLikedNews
        fields = ['headline', 'link', 'source', 'id',]
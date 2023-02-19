from django.test import TestCase
import pytz
import requests
import os
from datetime import datetime
from base.models import NewsArticle

class RedditApiTestCase(TestCase):
    '''
    This class tests the Reddit API endpoint for status code, content type and data.
    '''
    
    def test_api_endpoint(self):
        url = os.getenv('REDDIT_API_URL')
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("data" in response.json())
        
        
class NewsApiTestCase(TestCase):
    '''
    This class tests the News API endpoint for status code, content type and data.
    '''
    
    def test_api_endpoint_1(self):
        url = os.getenv('NEWS_API_HEADLINES_URL')
        url += f'&apiKey={os.getenv("NEWSAPI_KEY")}&sortBy=popularity'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("articles" in response.json())
        
    def test_api_endpoint_2(self):
        url = os.getenv('NEWS_API_URL')
        url += f'?q=bitcoin&apiKey={os.getenv("NEWSAPI_KEY")}&sortBy=popularity'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("articles" in response.json())
        
        
class DatabaseTestCase(TestCase):
    '''
    This class tests the database for data.
    '''
    
    def test_create_instance(self):
        instance = NewsArticle(headline="Test", 
                               link="https://www.test.com", 
                               source="test", 
                               published_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
                               fetched_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        instance.save()
        self.assertIsNotNone(instance.article_id)
        self.assertEqual(instance.headline, "Test")
        self.assertEqual(instance.link, "https://www.test.com")
        self.assertEqual(instance.source, "test")
        self.assertEqual(instance.published_at, datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        self.assertEqual(instance.fetched_at, datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
    
    def test_retrieve_instance(self):
        instance = NewsArticle(headline="Test", 
                               link="https://www.test.com", 
                               source="test", 
                               published_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
                               fetched_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        instance.save()
        retrieved_instance = NewsArticle.objects.get(article_id=instance.article_id)
        self.assertEqual(instance, retrieved_instance)
    
    def test_update_instance(self):
        instance = NewsArticle(headline="Test", 
                               link="https://www.test.com", 
                               source="test", 
                               published_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
                               fetched_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        instance.save()
        instance.headline = "updated"
        instance.save()
        retrieved_instance = NewsArticle.objects.get(article_id=instance.article_id)
        self.assertEqual(retrieved_instance.headline, "updated")
        
    def test_delete_instance(self):
        instance = NewsArticle(headline="Test", 
                               link="https://www.test.com", 
                               source="test", 
                               published_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
                               fetched_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        instance.save()
        instance.delete()
        with self.assertRaises(NewsArticle.DoesNotExist):
            NewsArticle.objects.get(article_id=instance.article_id)

    def test_query_instances(self):
        instance1 = NewsArticle(headline="ABC", 
                                link="https://www.test.com", 
                                source="test", 
                                published_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
                               fetched_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        instance1.save()
        instance2 = NewsArticle(headline="XYZ", 
                                link="https://www.test.com", 
                                source="test", 
                                published_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
                               fetched_at=datetime(2020, 1, 1, 0, 0, 0, tzinfo=pytz.UTC))
        instance2.save()
        instances = NewsArticle.objects.filter(headline="XYZ")
        self.assertEqual(len(instances), 1)
        self.assertEqual(instances[0], instance2)
from django.test import TestCase
import requests
import os

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
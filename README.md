# News Aggregator

News Aggregator is a project developed using Django-REST framework. As the name suggests, the project aims to aggregate news articles from various external APIs. It is a submission for the backend position at Stellic. The project utilizes external APIs to fetch news articles and provides an endpoint for users to retrieve the aggregated list of top 10 articles from Reddit and News API. In addition to this, the project also includes an endpoint for users to favorite news articles by specifying their ID and user name. The project is designed to fullfil the requirements specified in the problem description. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Expiry Rate Feature](#expiry-rate-feature)
- [Assumptions](#assumptions)
- [External APIs](#external-apis)
- [Project Architecure](#project-architecure)
- [Testing](#testing)
- [Remarks](#remarks)

## Installation

Here's a step-by-step guide on how to set up a Django project named "NewsAggregator":

1. Clone the repository to your local machine:
`git clone https://github.com/FaazAbidi/News-Aggregator.git`

2. Install the project dependencies:
`pip install -r requirements.txt`

3. Start the development server:
`python manage.py runserver`

The project should now be available at http://localhost:8000/.

## Usage

This API is designed to aggregate data from two external sources: Reddit and News API. The primary aim of the API is to provide users with a platform to fetch news articles and search for news articles with similar headlines. The `news/` endpoint also maintains an expiry limit for all the results. If request is past the expiry limit, it fetches from the external APIs else it retrieves from the database. It provides a good balance between performance and relevance.

Apart from fetching news articles, the API allows users to mark articles as favorites. Users can mark articles as favorites by sending a `POST` request to the `/news/favourite/` endpoint, which accepts the article `id` and the `user` name as parameters. Similarly, users can retrieve all their favorite articles by sending a `GET` request to the `/news/favourite/` endpoint with `user` as a parameter.

Below are the details of all the endpoints available.

### Endpoints

1. #### `/`

This endpoint is a landing page for the API with a welcome message.

**Method**: `GET`

**URL Parameters**: None

**Request Body**: None

**Response Body**: 
```
{
  "message": "Welcome to News Aggregator API"
}
```

2. #### `/news/`

This endpoint fetches a list of news articles either from the database or external APIs based on the expiry limit. It also provides support for searching through the query parameter to filter news articles based on search criteria.

**Method**: `GET`

**URL Parameters**: `query`

**Request Body**: None

**Response Body**: 
```
[
  {
    "headline": "More Ransomware Victims Are Refusing to Pay Hackers",
    "link": "https://gizmodo.com/ransomware-hackers-blockchain-chainalysis-1850005764",
    "source": "newsapi"
   },
  {
    "headline": "N.J. man hired hitman for $20K in Bitcoin to kill a 14-year-old, prosecutors say",
    "link": "https://www.nbcnews.com/news/us-news/new-jersey-man-hired-hitman-paid-20k-bitcoin-kill-14-year-old-prosecut-rcna68971",
    "source": "reddit"
    },
]
```


3. #### `/news/favourite/`

This endpoint allows users to toggle their favorite news articles by specifying the article id and their name. The endpoint then retrieves the updated news article with the updated favorite value.

**Method**: `POST`

**URL Parameters**: `user: str & id: int`  

**Request Body**: None

**Response Body**: 
```
{
  "headline": "More Ransomware Victims Are Refusing to Pay Hackers",
  "link": "https://gizmodo.com/ransomware-hackers-blockchain-chainalysis-1850005764",
  "source": "newsapi",
  "favourite" : true,
  "id" : 201
}
```
                      
 4. #### `/news/favourite/`

This endpoint retrieves a list of all favourite news articles of the specified user.

**Method**: `GET`

**URL Parameters**: `user: str`  

**Request Body**: None

**Response Body**: 
```
[
  {
    "headline": "More Ransomware Victims Are Refusing to Pay Hackers",
    "link": "https://gizmodo.com/ransomware-hackers-blockchain-chainalysis-1850005764",
    "source": "newsapi",
    "favourite" : true,
    "id" : 201
   },
   {
    "headline": "N.J. man hired hitman for $20K in Bitcoin to kill a 14-year-old, prosecutors say",
    "link": "https://www.nbcnews.com/news/us-news/new-jersey-man-hired-hitman-paid-20k-bitcoin-kill-14-year-old-prosecut-rcna68971",
    "source": "reddit"
    "favourite" : true,
    "id" : 187
    },
]
```

## Database Schema

The database schema for this project was created based on the problem description and requirements. The schema consists of two main entities - Users and Articles - and a third entity, Favourite Articles, to resolve the many-to-many relationship between Users and Articles.

I created the ERD for this schema using an online tool called drawSQL. The schema was designed to be simple and intuitive, while still meeting all the necessary requirements. This schema was then mapped directly to the Django models used in the project.

To implement the schema, SQLite was used, as it was required in the assessment. The database schema was designed to be easily scalable, allowing for the addition of new entities or attributes as needed. The schema was also designed with data consistency and integrity in mind, to ensure that all data stored in the database is accurate and reliable.

<img src="https://i.ibb.co/ZXnpmCB/schema.png" alt="Schema" style="height: 300px; width:600px;"/>

You can also access the ERD [Here](https://drawsql.app/teams/doxa/diagrams/newsaggregator)

## Expiry Rate Feature

One of the required features for this API was to store the data from the API into a database such that, if a request is repeated, the response is returned from the database and does not need a new API call. It can be achieved, as suggested in the description, by some expiry limit. If request is past the expiry limit then fresh call is made. 

To implement this feature, I designed my schema to include a `fetched_at` column in the `news_article` table. This column is updated for each row that's part of the response whenever there is a fetch request from the database, allowing for easy tracking of whether the expiry limit has passed or not. When a new request comes in, the system checks the `last_fetched` value from the latest news article entry and compares it with the current time using `datetime.now()`. I have currently set the expiry limit to be `5 minutes`.

## Assumptions

There were a few ambiguities in the problem description, so, a few assumptions were made to execute this project.

It was not clear whether it's required to enter users in the database or not. Since we are storing user's favorites, it was assumed that there should be an entity for users for storing user's data. However, the issue with this is that we don't have a proper identifier for a user. From the endpoint, we are accessing users based on their names not on their ID, which is not ideal if users with the same names will use this API.

Another ambiguity was similar to the former. It was not clear when to create new users. Therefore, I decided to create a new user when there's a new name comes as a parameter through the `/news/favorite/` endpoint.

Lastly, in the sample requests provided, an auth token was included, but it was not mentioned anywhere in the project description. As a result, I assumed that an auth token is not required for the endpoints and did not implement it in the API.

## External APIs

As mentioned before, this api aggregates news articles from two external APIs, namely [Reddit](https://www.reddit.com/r/news/) (via the [Pushshift](https://github.com/pushshift/api) wrapper) and [NewsAPI](https://newsapi.org/). In particular, the `news/` endpoint of the API fetches news articles from NewsAPI and returns a list of the top 10 articles, which are then combined with the top 10 articles fetched from the Reddit endpoint.

To fetch the news articles, I used the official News API which provides access to various news sources worldwide. The Reddit endpoint, on the other hand, uses the Pushshift API, which provides a more flexible and efficient way of accessing Reddit data.

Note that for both endpoints, I am only taking the top 10 articles from each API, which should provide a good balance between relevance and performance.

1. Reddit (PushShift): `https://api.pushshift.io/reddit/search/submission?subreddit=news`
2. NewsApi: `https://newsapi.org/v2/everything` & `https://newsapi.org/v2/top-headlines?country=us` 

## Project Architecure

The project follows the Django MVT (Model-View-Template) architecture for the most part. I created two Django apps to organize the code, one for the API named `api` and the other for models and other things named `base`. The `api` app is kept isolated, so it's easy to test and reuse.

To decouple the views and to keep the code maintainable and extensible, I implemented a little of the repository architecture. I created repository modules for both the models, which abstracts away the data access from views. It doesn't matter to `views.py` whether the data is coming from the database or external APIs. This helped to keep the code more decoupled and easy to maintain.

## Testing

To ensure the stability and reliability of the application, I implemented a suite of unit tests. There are 8 unit tests in total, focused on external API calls and database CRUD operations.

The first set of tests were for the external APIs used in the application, which are Pushshift API for Reddit and News API. These tests include verifying the status code of the response and the format of the returned data. The tests ensure that the application can handle different responses from the external APIs and can parse the data correctly.

The second set of tests were for the database operations. The tests covered create, update, insert, delete, and query operations for the models in the application. These tests ensure that the database operations are executed properly and the models are functioning as expected.

Overall, these tests provide a good level of confidence that the application is working as intended and that any changes or updates will not cause unexpected issues. Coverage of these are not that much and it can surely be increased.

## Remarks

I hope I am able to demonstrate my skills effectively considering the limited time I spent on this. If there's any query related to this project, please reach out to me. I look forward to your feedback!

Note: I have intentionally pushed `.env` file for the demonstration. It's not advised to so.

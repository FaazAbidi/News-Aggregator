# News Aggregator

News Aggregator is Django-REST API. It uses external news APIs and aggregate the results of both. This is my submission for the Stellic Assessment test. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Assumptions](#assumptions)
- [External APIs](#external-apis)
- [Project Architecure](#project-architecure)
- [Testing](#testing)

## Installation

Instructions on how to install your project, including any prerequisites that need to be installed. This could include details on how to install any dependencies, how to set up a virtual environment, or any other steps that need to be taken.

1. Clone the repository to your local machine:
`git clone https://github.com/your-username/your-project.git`

2. Install the project dependencies:
`pip install -r requirements.txt`

3. Start the development server:
`python manage.py runserver`

The project should now be available at http://localhost:8000/.

## Usage

ssadsadsad

### Endpoints

1. #### `/news/`

This endpoint retrieves a list of all books in the database.

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
   }
]
```


2. #### `/news/favourite/`

This endpoint retrieves a list of all books in the database.

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
                      
 3. #### `/news/favourite/`

This endpoint retrieves a list of all books in the database.

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
   }
]
```

## Database Schema

The database schema for this project was created based on the problem description and requirements. The schema consists of two main entities - Users and Articles - and a third entity, Favourite Articles, to resolve the many-to-many relationship between Users and Articles.

I created this schema using an online tool called drawSQL. The schema was designed to be simple and intuitive, while still meeting all the necessary requirements. This schema was then mapped directly to the Django models used in the project.

To implement the schema, SQLite was used, as it was required in the assessment. The database schema was designed to be easily scalable, allowing for the addition of new entities or attributes as needed. The schema was also designed with data consistency and integrity in mind, to ensure that all data stored in the database is accurate and reliable.

<img src="https://i.ibb.co/ZXnpmCB/schema.png" alt="Schema" style="height: 300px; width:600px;"/>

You can also access the ERD [Here](https://i.ibb.co/ZXnpmCB/schema.png)

## Assumptions

There were a few ambiguities in the problem description, so, a few assumptions were made to execute this project.

It was not clear whether it's required to enter users in the database or not. Since we are storing user's favorites, it was assumed that there should be an entity for users for storing user's data. However, the issue with this is that we don't have a proper identifier for a user. From the endpoint, we are accessing users based on their names not on their ID, which is not ideal if users with the same names will use this API.

Another ambiguity was related to this as well. It was not clear when to create new users. Therefore, a new user is created when there's a new name that comes as a parameter through the favorite endpoint.

## External APIs

This api aggregates news articles from two external APIs, namely Reddit (via the Pushshift wrapper) and News API. In particular, the News endpoint of the API fetches news articles from News API and returns a list of the top 10 articles, which are then combined with the top 10 articles fetched from the Reddit endpoint.

To fetch the news articles, I used the official News API which provides access to various news sources worldwide. The Reddit endpoint, on the other hand, uses the Pushshift API, which provides a more flexible and efficient way of accessing Reddit data.

Note that for both endpoints, I am only taking the top 10 articles from each API, which should provide a good balance between relevance and performance.

1. Reddit (PushShift): `https://api.pushshift.io/reddit/search/submission?subreddit=news`
2. NewsApi: `https://newsapi.org/v2/everything` & `https://newsapi.org/v2/top-headlines?country=us` 

## Project Architecure

The project follows the Django MVT (Model-View-Template) architecture for the most part. I created two Django apps to organize the code, one for the API and the other for models and other things. The API app is kept isolated, so it's easy to test and reuse.

To decouple the views and to keep the code maintainable and extensible, I implemented a glimpse of the repository architecture. I created repository modules for both the models, which abstracts away the data access from views. It doesn't matter to views.py whether the data is coming from the database or external APIs. This helped to keep the code more decoupled and easy to maintain.

## Testing

To ensure the stability and reliability of the application, I implemented a suite of unit tests. There are 8 unit tests in total, focused on external API calls and database CRUD operations.

The first set of tests were for the external APIs used in the application, which are Pushshift API for Reddit and News API. These tests include verifying the status code of the response and the format of the returned data. The tests ensure that the application can handle different responses from the external APIs and can parse the data correctly.

The second set of tests were for the database operations. The tests covered create, update, insert, delete, and query operations for the models in the application. These tests ensure that the database operations are executed properly and the models are functioning as expected.

Overall, these tests provide a good level of confidence that the application is working as intended and that any changes or updates will not cause unexpected issues. Coverage of these are not that much and it can surely be increased.

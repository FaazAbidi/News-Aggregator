# News Aggregator

A brief description of your project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Database Schema](#database-schema)
- [Assumptions](#assumptions)
- [External APIs](#external-apis)
- [Design Patterns](#design-patterns)
- [Testing](#testing)
- [License](#license)

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

This is a simple Django based API. It has only two endpoints. Below are the details of them.

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

## Design Patterns

Details on any design patterns used in your project. This could include information on the pattern, why it was chosen, and how it was implemented.

## Testing

Instructions on how to contribute to your project, including details on how to submit bug reports, feature requests, or pull requests.

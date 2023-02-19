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

Details on the database schema used in your project. This could include information on tables, fields, relationships, or any other relevant details.

## Assumptions

Any assumptions made in the development of your project. This could include assumptions about user behavior, system requirements, or any other relevant details.

## Design Patterns

Details on any design patterns used in your project. This could include information on the pattern, why it was chosen, and how it was implemented.

## Testing

Instructions on how to contribute to your project, including details on how to submit bug reports, feature requests, or pull requests.

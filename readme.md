# AppStore program

## Introduction

app_store Application to display the list of software in the app store. This project is developed using Flask framework for Python, SQLite database and Bootstrap front-end framework.

## Design

### Database Design

The application uses a SQLite database to store the application and application description data. The specific database design is as follows.


#### app_store table

| Listings               | type    | describe            |
| ------------------| --------|----------------|
| id                | INTEGER | Self-growing ID      |
| app_id            | INTEGER | Application ID      |
| track_name        | TEXT    | Application Name    |
| size_bytes        | INTEGER | Application Size（Bytes） |
| currency          | TEXT    | Currency Type         |
| price             | REAL    | price            |
| rating_count_tot  | INTEGER | Total number of ratings for all versions |
| rating_count_ver  | INTEGER | Total number of ratings for the current version |
| user_rating       | REAL    | User ratings for all versions |
| user_rating_ver   | REAL    | User ratings for current version |
| ver               | TEXT    | Application Versions    |
| cont_rating       | TEXT    | Content Ratings        |
| prime_genre       | TEXT    | Main Type        |
| sup_devices_num   | INTEGER | Number of supported devices    |
| ipadSc_urls_num   | INTEGER |Number of iPad screenshots    |
| lang_num          | INTEGER | Number of languages        |
| vpp_lic           | INTEGER | VPP Licensing         |

#### app_store_desc Table

| Listings       | type     | describe          |
| -----------| --------|--------------|
| id         | INTEGER | Self-growing ID    |
| app_id     | INTEGER | Application ID    |
| app_desc   | TEXT    | Application  describe |

### Front-end design

The application was designed using the Bootstrap front-end framework and includes the following pages:

- index.html：Used to display the list of applications.
- detail.html：Used to display application details.

### Back-end design

The application is designed using Python's Flask framework and includes the following components.

- Flask application: used to handle HTTP requests and responses.
- SQLite database: for storing application and application description data.
- Flask Paginate library: used for pagination processing.
- Faker library: for random data generation.
- csv Library: for reading csv files.

## Development

### Installing dependencies

Before starting development, the following dependencies need to be installed.

```shell
pyenv local 3.7.0
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install Faker
pip install flask
pip install Flask-Paginate
pip install behave
pip install selenium
pip install gunicorn
pip freeze > requirements.txt
```
###Development and testing based on front-end and back-end design
The project uses Behave and Selenium for automated testing, and tests can be run using the following commands:

    behave
The test cases are located under the features folder.



##Installation
Clone or download the project code at:
```shell
git clone https://github.com/your_username/app.git
```
To access the project catalog:
```shell
cd app
```
Create and activate the Python virtual environment:
```shell
python3 -m venv .venv
source .venv/bin/activate
```
Install the Python dependencies required for the project:
```shell
pip install -r requirements.txt
```
Initialize and import data
```shell
python3 arse_csv.py
```
Run the application (codio run as an example)
```shell
export FLASK_APP=app.py

python3 -m flask run -h 0.0.0.0
```


Visit the following URL in a web browser to view the application:
    
    http://localhost:5000/

##using
1. This page will show the list of applications. You can click the "Details" button to view the details of the application.
2. On the application list page, you can use the paging control to browse different pages of applications.
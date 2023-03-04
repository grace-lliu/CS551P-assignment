# Introduction

**What is it **

app_store Application to display the list of software in the app store. This project is developed using Flask framework for Python, SQLite database and Bootstrap front-end framework.


## Main Features

**1,List page：This page will show the list of applications. You can click the "Details" button to view the details of the application. **

**2,Details page：This page will show the  application's related Information, You can click the "return" button to go back the list page. **

**3,Paging component: each page displays eight data, you can click on the specified number of pages, it will jump to the corresponding page. **


## Installation
Clone or download the project code at:
```shell
git clone https://github.com/grace-lliu/CS551P-assignment.git
```
To access the project catalog:
```shell
cd CS551P-assignment
```
install and set the local version of Python to 3.7.0 using the pyenv version manager.

``` shell
pyenv instal1 3.7.8
pyeny local 3.7.0
```

Create and activate the Python virtual environment:
```shell
python3 -m venv .venv
source .venv/bin/activate
```
Install the Python dependencies required for the project:
```shell
pip install --upgrade pip
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



## Running the application
### Codio Running the application
```shell

export FLASK_APP=staff.py

python3 -m flask run -h 0.0.0.0
```
### Local operation Running the application
```shell
export FLASKAPP=staff.py

python3 -m flask run
```
### Render Running the application

1.Open address https://render.com/ Register Login

2.Click Dashboard Click "NEW" "Web Service"

3.Connect our repository

4.Fill in as follows (eg:)
```shell
name: Lw-staff
Environment: Python3
Build command: ＄ pip install -r requirements.txt Start 
command: $ gunicorn staff:app
```
5.Click 'Create Web Service'

6.Until build successfully

7.Access: https:/lw-staff.onrender.com/

## Test
Run the behave command to see the results
```shell
behave
```

![image](https://github.com/grace-lliu/studyInAberdeen/blob/master/197671677941555_.pic.jpg)


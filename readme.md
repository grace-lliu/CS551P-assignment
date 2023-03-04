## Introduction
** What is it **
app_store application displays a list of software in the application store. 
The project uses Flask framework for Python, faker to supplement the data, 
SQLite database and Bootstrap front-end framework for database development.

### Main Features
1,display all the data of the queried application
2,On the application list page, you can use the paging control to browse different pages of applications. paging function: each page shows eight pieces of data
3,each data can click on the details to see the application of the relevant information.You can click the "Details" button to view the details of the application.
4,Click the back button to return to the main page

### Installation
Clone or download the project code at:
```shell
git clone https://github.com/grace-lliu/CS551P-assignment.git
```
To access the project catalog:
```shell
cd CS551P-assignment
```

install and set the local version of Python to 3.7.0 using the pyenv version manager.
```shell
pyenv install 3.7.0
pyenv local 3.7.0
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
## Run the Application
### Codio Running the application
```shell
export FLASK_APP=app.py

python3 -m flask run -h 0.0.0.0
```
### Local operation Running the application
```shell
export FLASK_APP=app.py

python3 -m flask run 
```
## Visit the following URL in a web browser to view the application:
    
    http://localhost:5000/

## Render Running the application

1.Open address https://render.com/ Register Login

2.Click Dashboard Click "NEw","Web Service"

3.Connect our repository

4.Fill in as follows (eg:)
```shell
name: ali-cs551-assignment
Environment: Python3
Build command: $ pip install -r requirements.txt
Start command: $ gunicorn index:app
```
5.Click 'Create Web Service'
6.Until build successfully
7.Access：https://lw-staff.onrender.com/
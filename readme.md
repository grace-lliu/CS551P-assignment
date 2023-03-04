##Installation
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

##using
1. This page will show the list of applications. You can click the "Details" button to view the details of the application.
2. On the application list page, you can use the paging control to browse different pages of applications.


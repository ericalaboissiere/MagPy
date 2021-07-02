# MagPy
Version 1.0.0
Platform designed to ensure that all Python projects are using the latest available versions of the packages, in which it's possible receives a project name, a list of packages and returns the latest version of each package. This is only the backend API.

## Getting started

$ git clone MagPy

$ python -m venv venv

$ source venv/bin/activate

$ pip freeze > requirements.txt

$ pip install -r requirements.txt

$ ./manage.py runserver



## Deploying / Publishing

The project was deployed on heroku
Click [here](https://mag-py.herokuapp.com/) to visit the project

## Routes


POST /api/projects - creates project
GET /api/projects/name - list project by name
DELETE /api/projects/name - delete cproject by name

## Examples of Requests:

Creating project: POST /api/projects


```{
"name": "titan"
"packages": [
{"name": "Django"},
{"name": "graphene", "version": "2.0"}
]
}
```

Getting project by name: GET /api/projects/titan

Deleting project by name: DELETE /api/projects/titan

## Running the tests at port 8000:

k6 run -e API_BASE='http://localhost:8000/' tests-open.js


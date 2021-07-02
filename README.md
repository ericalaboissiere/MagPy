MagPy
Version 1.0.0
Platform designed to ensure that all Python projects are using the latest available versions of the packages, in which it's possible receives a project name, a list of packages and returns the latest version of each package. This is only the backend API.

Getting started

git clone MagPy
Use pip to install Pipenv:

$ pip install --user pipenv

$ pip install virtualenv

'''pip freeze > requirements.txt
pip install -r requirements.txt'''

cd kmdb
docker-compose up

Deploying / Publishing
The project was deployed on heroku
Click here to visit the project
Routes

POST /api/projects - creates project
GET /api/projects/name - list project by name
DELETE /api/projects/name - delete cproject by name

Examples of Requests:

Creating project: POST /api/projects

{
"name": "titan"
"packages": [
{"name": "Django"},
{"name": "graphene", "version": "2.0"}
]
}

Getting project by name: GET /api/projects/titan

Deleting project by name: DELETE /api/projects/titan

Running the tests:
Execute TEST=TEST python manage.py test

# django-training

## This is a music platform on which artists can sign up and put up their albums for sale.

## setup

- clone the repo
- cd into the project folder
- download poetry
- to use the venv use `poetry shell`
- to install the defined dependencies for your project, just run `poetry install`
- to run the project `python manage.py runserver`
- to make superuser to access the admin dashboard `python manage.py createsuperuser`
- run `redis-server` command
- run `celery -A musicplatform worker -B -l info` command
- set env variables(SECRET_KEY, redis_url and email cradentials (email, password))

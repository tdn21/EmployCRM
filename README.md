# Medicento Employ CRM

This project is a django based CRM application providing dashboard for employees and easy management of employees for admins

## Local Apps

* students
* colleges
* links
* profiles

### DB Models

All models are available in students/models.py file

### URLS

Each app has its own url namespace, so concerned urls can be found in app_name/urls.py

### Views

Views corresponding to each app can be found in app_name/views.py


### How to setup local project
Run these commands in your command line

* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver
# blog-legendary-eureka

## Commands to start the project
1. `python -m pip install django`  Install django - to install specific for this project use `python -m pip install django==3.0`.
2. To pin the dependencies `python -m pip freeze > requirements.txt` i.e. to write the names and versions of all external python dependencies.
3. To install all dependencies in the requirements.txt in one command `python -m pip install -r requirements.txt`.
4. To start the project, move to your desired location and run `django-admin startproject BLOG`.
5. To start an app use the command `python manage.py startapp <appname>`.
6. The startapp command is used while in the root project folder i.e. /BLOG/ where `manage.py` is found. 

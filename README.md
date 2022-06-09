# SUPER USER

- user jmarinarango
- pass 2020



# ADMIN COMMANDS

For startapp commando you should register you app in settings.py file, in the array INSTALLED_APPS, later add [project]/urls.py to [app]/urls.py

    python3 manage.py runserver
    python3 manage.py shell
    python3 manage.py createsuperuser
    django-admin startproject [NAME]    # CREATE PROJECT (settings)
    python3 manage.py startapp [NAME] 	# DJANGO APP of project (MVC)
    django-admin startapp [NAME]        # DJANGO APP

- [GRAPPELLLI ](https://github.com/sehmaschine/django-grappelli) Change Django styles-library
- [Django - libraries admin styles](https://djangopackages.org/grids/g/admin-styling/)

# MIGRATIONS

    python3 manage.py migrate
    python3 manage.py makemigrations
    python3 manage.py makemigrations first_app
    python3 manage.py sqlmigrate first_app 0001
    python3 manage.py migrate





## CONSOLE (DJANGO SHELL)

    python manage.py shell

    from first_app.models import Choice, Question
    from django.utils import timezone

    Question.objects.all()
    q = Question(question_text='pregunta 1', pub_date=timezone.now())
    q.save()

# DB / MODELS

- Add models to dash: 
  - [Documentation](https://docs.djangoproject.com/en/4.0/intro/tutorial07/) 
  - In admin.py [project](first_app/admin.py)
- [Django databases](https://docs.djangoproject.com/en/4.0/ref/databases/)
- [Many to Many relationship](https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django)



# REST API
- **Serializers**: Allow you to convert a class in json or xml format, they can validate any data, it's like the data structure  
  - [Example](/apps/dash_app/serializer.py)
  - 
- **ViewSets (Controllers)**: CRUD you can overrided some element of the CRUD
  - [Documentation](https://www.django-rest-framework.org/api-guide/viewsets/)
  - [Better Documentation](https://testdriven.io/blog/drf-views-part-3/)
  - @action allows you to have a custom routing for an specific action viewset/1/action
  - [Parsers: allow multipart data](https://www.django-rest-framework.org/api-guide/parsers/)
- JWT (JSON WEB TOKEN) digital signature
  - [simple JWTF](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [SIMPLEJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) 
  - Simple ways
- [DRF DJANGO REST FRAMEWORK](https://www.django-rest-framework.org/) / types of authentication HARDCORE!! 
  - BasicAuthentication: Validated user and password
  - SessionAuthentication
  - TokenAuthentication: Unique token per user
- [Code example](https://github.com/developerpe/ecommerce_rest)
- Simple history: allow to track all the user actions [Docs](https://django-simple-history.readthedocs.io/en/latest/)
- [All classes and methods](https://www.cdrf.co/)


# PROJECT STRUCTURE
- You can change the project structure by creating all the apps inside /apps
  - Add in settings.py sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
  - In INSTALLED_APPS add apps.[APP_NAME]

# FORMS

- It's better use crispy forms for templates
- [Messages framework](https://docs.djangoproject.com/en/4.0/ref/contrib/messages/), [example](/comment_app/templates/comment_app/contact.html)

# TEMPLATES
- URLS should be [project / url_namespace](comment_app/templates/comment_app/update.html)
- Bootstrap [you can use bootstrap in your code](https://data-flair.training/blogs/django-bootstrap/)
  - [Example](comment_app/templates/comment_app/contact.html)
  - [Crispy forms](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html)
  - With forms and files is necesary to use multipart/form-data 
- Filters working by each value (rendering values adding something) {{ value|add:'2'}}



# LOGGING

- [Documentation](https://docs.djangoproject.com/en/4.0/topics/logging/)

# DEBUGGING

- [DJANGO DEBUG TOOLBAR](https://django-debug-toolbar.readthedocs.io/en/latest/)




# TEST

    python3 manage.py test Polls/tests


#  TIPS

- Imports are related to manage.py
  - [Example an import from another app](Polls/views.py)

# DOCUMENTATION 

- [swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html)
  - [Explain video](https://www.youtube.com/watch?v=FvRfzQREXAY&t=1523s&ab_channel=Developer.pe)
  - Swagger search for viewsets.ModelViewSet and build the documentary automatically
- FILES INVOLVED 
  - [urls.py](dash_django/urls.py)
  - [settings.py](dash_django/settings.py)
  - [viewset.py](dash_app/viewsets.py)



# DASH API

Our project will have the next db structure

![alt text](images/model.png)

  




# DJANGO - JUPYTER

[Reference](https://stackoverflow.com/questions/35483328/how-do-i-set-up-jupyter-ipython-notebook-for-django/54856080#54856080)

- Install jupyter



      pip install jupyter


Install django-extentions

    pip install django-extensions

Set up django-extensions by adding it to the INSTALLED_APPS setting of your Django project settings.py file.:

    INSTALLED_APPS = (
      ...
      'django_extensions',
    )


Run the shell_plus management command that is part of django-extensions. Use the option --notebook to start a notebook:

    python3 manage.py shell_plus --notebook




Jupyter Notebooks will open automatically in your browser.




# MODIFING manage.py
- Search for python-dotenv read .env
- Catch custom error: DjangoImportException



# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip
https://www.vaultproject.io/
https://gpgtools.org/
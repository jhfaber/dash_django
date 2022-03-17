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


# MIGRATIONS

    python3 manage.py migrate
    python3 manage.py makemigrations
    python3 manage.py makemigrations first_app
    python3 manage.py sqlmigrate first_app 0001
    python3 manage.py migrate


    


## CONSOLE

    python manage.py shell

    from first_app.models import Choice, Question
    from django.utils import timezone

    Question.objects.all()
    q = Question(question_text='pregunta 1', pub_date=timezone.now())
    q.save()

# DB



# COMMOND TASK / TIPS

- Imports are related to manage.py
- Add models to dash: 
  - [Documentation](https://docs.djangoproject.com/en/4.0/intro/tutorial07/) 
  - In admin.py [project](first_app/admin.py)
- [Django databases](https://docs.djangoproject.com/en/4.0/ref/databases/)
- [Django REST FRAMEWORK](https://www.django-rest-framework.org/)
- Serializers: Allow you to convert a class in json or xml format, they can validate any data, it's like the data structure
- ViewSets (Controllers): CRUD you can overrided some element of the CRUD




# TEST

    python3 manage.py test Polls/tests

# CONCEPTS

- Generic views are views with classes
  
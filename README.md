# Django-4-By-Example-Blog
This is my exercise based on Django 4 By Example
Github link: https://github.com/gurnitha/Django-4-By-Example-Blog


## 01. Preparations

#### 01.1 Create Github repository

        modified:   .gitignore
        modified:   README.md

        Activities:

        1. Modified .gitignore file
        2. Modified Readme file
        3. Git commit and pushed it to Github


#### 01.2 Creating a Python virtual environment

        > python --version
        > pip --version
        > virtualenv --version
        > python -m venv venv3941
        git push origin
        Enter passphrase for key '/c/Users/hp/.ssh/id_rsa':

        modified:   README.md


#### 01.3 Installing Django

        > .\venv3941\Scripts\activate
        (venv3941) .../Blog>
        > pip install Django~=4.1.0
        > python -m django --version
          4.1.5
        > git add .
        > git status
        modified:   README.md
        > git commit -m "01.3 Installing Django"



## 02. Creating Django Project

#### 02.1 Creating your first project

        > django-admin startproject mysite .

        modified:   README.md
        new file:   manage.py
        new file:   mysite/__init__.py
        new file:   mysite/asgi.py
        new file:   mysite/settings.py
        new file:   mysite/urls.py
        new file:   mysite/wsgi.py


#### 02.2 Applying initial database migrations

        > python manage.py migrate

        Operations to perform:
        Running migrations:
          Applying contenttypes.0001_initial... OK
          Applying auth.0001_initial... OK
          Applying admin.0001_initial... OK
          Applying admin.0002_logentry_remove_auto_add... OK
          Applying admin.0003_logentry_add_action_flag_choices... OK
          Applying contenttypes.0002_remove_content_type_name... OK
          Applying auth.0002_alter_permission_name_max_length... OK
          Applying auth.0003_alter_user_email_max_length... OK
          Applying auth.0004_alter_user_username_opts... OK
          Applying auth.0005_alter_user_last_login_null... OK
          Applying auth.0006_require_contenttypes_0002... OK
          Applying auth.0007_alter_validators_add_error_messages... OK
          Applying auth.0008_alter_user_username_max_length... OK
          Applying auth.0009_alter_user_last_name_max_length... OK
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK

        modified:   README.md


#### 02.3 Running the development serve

          Blog> python manage.py runserver
          Watching for file changes with StatReloader
          Performing system checks...

          System check identified no issues (0 silenced).
          January 11, 2023 - 08:31:56
          Django version 4.1.5, using settings 'mysite.settings'
          Starting development server at http://127.0.0.1:8000/
          Quit the server with CTRL-BREAK.

        modified:   README.md



## 03. Creating Django Application

#### 03.1 Creating an application

        > python manage.py startapp blog

        modified:   README.md
        new file:   blog/__init__.py
        new file:   blog/admin.py
        new file:   blog/apps.py
        new file:   blog/migrations/__init__.py
        new file:   blog/models.py
        new file:   blog/tests.py
        new file:   blog/views.py



## 04. Django Models: Creating the blog data models

#### 04.1 Creating the Post model

        modified:   README.md
        modified:   blog/models.py
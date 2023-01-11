# Django-4-By-Example-Blog
This is my exercise based on Django 4 By Example
Github link: https://github.com/gurnitha/Django-4-By-Example-Blog


# Chapter 1: Building a Blog Application


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


#### 04.2 Activating the blog application

        modified:   README.md
        modified:   mysite/settings.py


#### 04.3 Creating and applying migrations

        > python manage.py makemigrations blog
        > python manage.py sqlmigrate blog 0001

        BEGIN;
        --
        -- Create model Post
        --
        CREATE TABLE "blog_post" (
        	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
        	"title" varchar(250) NOT NULL, 
        	"slug" varchar(250) NOT NULL, 
        	"body" text NOT NULL, 
        	"publish" datetime NOT NULL, 
        	"created" datetime NOT NULL, 
        	"updated" datetime NOT NULL, 
        	"status" varchar(2) NOT NULL, 
        	"author_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
        --
        -- Create index blog_post_publish_bb7600_idx on field(s) -publish of model post
        --
        CREATE INDEX "blog_post_publish_bb7600_idx" ON "blog_post" ("publish" DESC);
        CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
        CREATE INDEX "blog_post_author_id_dd7a8485" ON "blog_post" ("author_id");
        COMMIT;

        modified:   README.md
        new file:   blog/migrations/0001_initial.py
        modified:   blog/models.py



## 05. Creating an administration site for models


#### 05.1 Creating a superuser

        > python manage.py migrate
        Blog> python manage.py createsuperuser
        Username (leave blank to use 'hp'): admin
        Email address: admin@admin.com
        Password: admin
        Password (again): admin
        The password is too similar to the username.
        This password is too short. It must contain at least 8 characters.
        This password is too common.
        Bypass password validation and create user anyway? [y/N]: y
        Superuser created successfully.

        modified:   README.md


#### 05.2 The Django administration site

        > python manage.py runserver
        Watching for file changes with StatReloader
        Performing system checks...

        System check identified no issues (0 silenced).
        January 11, 2023 - 09:30:23
        Django version 3.2, using settings 'config.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CTRL-BREAK.

        modified:   README.md


#### 05.3 Adding models to the administration site

        modified:   README.md
        modified:   blog/admin.py


#### 05.4 Customizing the models displayed

        modified:   README.md
        modified:   blog/admin.py



## 06. Working with QuerySets and managers


#### 06.1 Working with QuerySets

        Creating objects

        > python manage.py shell

        >>>from django.contrib.auth.models import User
        >>>from blog.models import Post
        >>> user = User.objects.get(username='admin')
        >>> post = Post(title='Another post',
        	...             slug='another-post',
        	...             body='Post body.',
        	...             author=user)
        >>> post.save()

        Updating objects

        >>> post.title = 'New title'>>> post.save()

        Retrieving objects

        >>> all_posts = Post.objects.all()

        >>> Post.objects.all()
        <QuerySet [<Post: Who was Django Reinhardt?>, <Post: New title>]>

        Using the filter() method

        >>> Post.objects.filter(publish__year=2022)

        >>> Post.objects.filter(publish__year=2022, author__username='admin')
        >>> Post.objects.filter(publish__year=2022) \
        >>>             .filter(author__username='admin'

        Using exclude()

        >>> Post.objects.filter(publish__year=2022) \
        >>>             .exclude(title__startswith='Why')

        Using order_by()

        >>> Post.objects.order_by('title')
        >>> Post.objects.order_by('-title')

        Deleting objects

        >>> post = Post.objects.get(id=1)
        >>> post.delete()

        modified:   README.md


#### 06.2 Model managers - Creating custom manager for models

        Blog> python manage.py shell
        ...
        >>> from blog.models import Post
        >>> Post.published.filter(title__startswith='who')
        <QuerySet [<Post: Who was Django Rainhard?>]>
        >>>
        modified:   README.md

        modified:   README.md
        modified:   blog/models.py

        Activities:

        1. Creating custom manager for Post model
        2. Tesing: using the python shell to test it
        3. Result: as seen above



## 07. Building List and Detail Views


#### 07.1 Creating post_list views

        modified:   README.md
        modified:   blog/views.py


#### 07.2 Creating post_detail views

        modified:   README.md
        modified:   blog/views.py



## 08. Creating URL patterns for the views


#### 08.1 Creating path for Blog post_list and post_detail

        modified:   README.md
        new file:   blog/urls.py


#### 08.2 Including Blog URL patterts in the main URL patterns

        modified:   README.md
        modified:   mysite/urls.py


## 09. Creating Templates for the Views


#### 09.1 Creating a base template

        modified:   README.md
        new file:   templates/blog/base.html


#### 09.2 Creating post list template

        modified:   README.md
        new file:   templates/blog/post/list.html


#### 09.3 Creating the post detail template

        modified:   README.md
        new file:   templates/blog/post/detail.html


#### 09.4 Moving templates to blog app

        modified:   .gitignore
        modified:   README.md
        new file:   _docs
        new file:   blog/templates/blog/base.html
        new file:   blog/templates/blog/post/detail.html
        new file:   blog/templates/blog/post/list.html
        deleted:    templates/blog/base.html
        deleted:    templates/blog/post/detail.html
        deleted:    templates/blog/post/list.html



## 10. Static Files


#### 10.1 Adding static files

        modified:   README.md
        new file:   blog/static/css/blog.css

        NOTE:

        1. Loding static files has been done previously
           in base.html
        2. Re-run the server to load the static files
        3. At this poin, path for the static files and
           templates did not activate yet due to
           we are working on local development.
        4. Result: it works

        modified:   README.md
        new file:   blog/static/css/blog.css


## 11. End Chapter 01

#### 11.1 Summary

        Activities:

        1. Learned basics of django framework
        2. Creating django project
        3. Creating django app
        4. Creating model
        5. Run and appply migrations
        7. Urls patterns
        8. Views
        9. Templates
        10. Loading static files

        modified:   README.md



# Chapter 2: Enhancing the Blog with Advance Features


## 01. Cannonical URLs and SEO Friendly URLs


#### 01.1 Using Cannonical URLs for models and back link

        modified:   README.md
        modified:   blog/models.py
        modified:   blog/templates/blog/post/detail.html
        modified:   blog/templates/blog/post/list.html

        Activities:

        1. In models.py import this: from django.urls import reverse
        2. In models.py define this:
        def get_absolute_url(self):
                return reverse('blog:post_detail',args=[self.id])
        3. Add back link to detail page


#### 01.2 Creating SEO-friendly URLs for posts

        modified:   README.md
        new file:   blog/migrations/0002_alter_post_slug.py
        modified:   blog/models.py

        Activities:

        1. Add this to slug field in models.py: 
           unique_for_date='publish')
        2. Run and apply migrations


#### 01.3 Modifying the URL patterns   

        modified:   README.md
        modified:   blog/urls.py

        Activities:

        1. Mofify the post detail url


#### 01.4 Modifying the post_detail views   

        modified:   README.md
        modified:   blog/views.py

        Activities:

        1. Modified post_detail view with this:

        def post_detail(request, year, month, day, post):
                post = get_object_or_404(Post,
                                        status=Post.Status.PUBLISHED,
                                        slug=post,
                                        publish__year=year,
                                        publish__month=month,
                                        publish__day=day) 



#### 01.5 Modifying the canonical URL for posts   

        modified:   README.md
        modified:   blog/models.py

        Activities:

        1. Modified get_absolute_url in Post model to this:

        def get_absolute_url(self):
                return reverse('blog:post_detail',
                        args=[self.publish.year,
                                  self.publish.month,
                                  self.publish.day,
                                  self.slug])
        2. Testing: re-run the server
        3. Result: the end-poin in the browser:
           http://127.0.0.1:8000/blog/2023/1/11/who-is-mr-antonio-mele/



## 02. Adding pagination 


#### 02.1 Adding pagination to the post list view  

        modified:   README.md
        modified:   blog/views.py


#### 02.2 Creating a pagination template

        modified:   README.md
        modified:   blog/templates/blog/post/list.html
        new file:   blog/templates/pagination.html


#### 02.3 Handling pagination errors - with integer parameter request

        Situation:

        1. Total posts in db: 7
        2. Posts per page: 3
        3. Max pages: 3
           http://127.0.0.1:8000/blog/?page=3
        4. > than max pages: 4
           http://127.0.0.1:8000/blog/?page=4

           Result: 

           EmptyPage at /blog/
           That page contains no results

        NEXT: Handling the EmptyPage error

        modified:   README.md
        modified:   blog/views.py

        NOTE:

        1. This solution could not handle if the request
           is not integer parameter, like this:
           http://127.0.0.1:8000/blog/?page=not-integer

           Error shows:

           PageNotAnInteger at /blog/

        NEXT: Handling non integer request parameter


#### 02.4 Handling pagination errors - with NON integer parameter request

        modified:   README.md
        modified:   blog/views.py



## 03. Building class-based views   


##### 03.1 Using a class-based view to list posts

        modified:   README.md
        modified:   blog/templates/blog/post/list.html
        modified:   blog/urls.py
        modified:   blog/views.py

        NOTE: 

        1. It has similar error as the previous one.
        2. This solution could not handle if the request
           is not integer parameter, like this:
           http://127.0.0.1:8000/blog/?page=not-integer
           and parameter like this:
           http://127.0.0.1:8000/blog/?page=4

           Error shows:

           Page not found (404)
           Page is not “last”, nor can it be converted to an int.
        3. Remember, this is just an alternative

        NEXT: Return to Function-Based Views




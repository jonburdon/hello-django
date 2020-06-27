# Gitpod To do

Based on Code Institute Tutorial

## Technologies
1. HTML
2. CSS
3. Python
4. Django

## Project Aims
1. Use built in Django CRUD functions to create a simple TODO App.

## Developer Aims 
1. Demonstrate simple django initial setup using github and gitpod
2. Implement basic CRUD functions
3. Include sufficient documentation (Readme and comments in code) to understand the above


## Project build process and build notes

### To Initiate:
https://github.com/Code-Institute-Org/gitpod-full-template and choose Use This template
install django using Pip:

`pip3 install django`

Create a django project called django_todo in the current folder:

`django-admin startproject django_todo .`

Note: the . opens the project in the current folder.

To run:

`python3 manage.py runserver`


To create new app:

`python3 manage.py startapp todo`

Open the views.py for this app. Views interface between the data and the front end.


Example:

`from django.shortcuts import render, HttpResponse

def say_hello(request):
    return HttpResponse("Hello!")`

Next edit urls.py in root project folder:

`from django.contrib import admin
from django.urls import path
from todo.views import say_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello, name="hello")
]`

Now the function in views_py will be available in root/hello

### Templates

Create folder called templates within project folder and subfolder called todo then filename.HTML
Example:
`templates/todo/todo_list.html`

NB in settings.py add this app to list of apps


## Commands for database changes and migrations

These commands update the python code so that it can make correct changes to the code for this project that handles the database.

`python3 manage.py makemigrations --dry-run` to dry run changes to database.

`python3 manage.py showmigrations`

`python3 manage.py migrate --plan` Show what the migrate will actually do, by using the plan flag.

`python3 manage.py migrate` Use for initial setup and then any future changes which will affect database handling. 

`python3 manage.py createsuperuser` To create superuser for this project

Go to project /admin to log in.

## Creating bespoke data models

`class Item():` is analagos to creating a 'sheet' in a spreadsheet. This will automatically create a new 'sheet' in the database when migrations are run.

EG:

`class Item(models.Model):`
`    name = models.CharField(max_length=50, null=False, blank=False)`
`   done = models.BooleanField(null=False, blank=False, default=False)`

Creates data table for Todos list with todo item and done field. NOTE id field is created automatically.

`python3 manage.py makemigrations --dry-run`

`python3 manage.py makemigrations`

This code will be converted to sql and run by python.

`python3 manage.py migrate --plan`

This now needs to be registered in Admin.py to make it visible in the admin panel.
eg:
``
from django.contrib import admin
from .models import Item

admin.site.register(Item)
``

Items will display as eg Item object (1) in database until we override the default inherrited name for fields in this row.

eg in models.py:

``
def __str__(self):
        return self.name
``


## Moving forward with creating html views:
To create new views after creating associated template, define them in views.py and update urls.py .


## Forms
Rather than creating the form ourself in html, django can create the form and then we add this as an input variable. The avoids input errors eg if the model marks something as required but then this is not marked as such in the html.

Therefore:
forms.py is created next and then `from .forms import ItemForm` is added in views.py

This will need to be added to the view.py file:

``
    form = ItemForm()
    context = {
        'form' : form
    }
``


## CRUD Functions

These were created in views.py
URLs for each function are defined in urls.py
todo_list.html contains the main functionality with edit_item.html and add_item.html containing from end templates and ui for those functions.

## Testing

tests.py is created automatically by django.

``
class TestDjango(TestCase):
    def test_this_thing_works(self):
        #test if 1 = 0 (this test should fail)
        self.assertEqual(1,0)

``

To run tests:
`python3 manage.py test`

Assertions such as equal, true, false and so on are used in django as in any other testing framework.


NOTE:
.FEF syntax means in this case tests pass, fail, error, fail

NOTE:
tests.py renamed to test_views.py to keep tests organised - these tests will jus test views.py 

`python3 manage.py test` runs all tests or the following syntax will run just one specific file:

`python3 manage.py test todo.test_forms`

Or run just a specific class of tests:

`python3 manage.py test todo.test_forms.TestItemForm`

OR run one specific test:

`python3 manage.py test todo.test_forms.TestItemForm.test_fields_are_explicit_in_metaclass`

### The Coverage tool shows what percentage of code is being tested

install:
`pip3 install coverage`

run:
`coverage run --source=todo manage.py test`

report is accessed via:
`coverage report`

interactive html report:
`coverage html`

Creates a folder called htmlcov

To view this in Gitpod `python3 -m http.server`

Open in browser, and view the file. For example if models.py is 89% tested the html report will highlight which parts of the code have not been tested.

After changes, need to run Coverage again, then regenerate the html report and check again whether all code has been tested.


## Deployment

Heroku cli is installed by default with some Gitpod templates.
It can be added by following this documentation: https://devcenter.heroku.com/articles/heroku-cli

Login to Heroku.com 
Then, in terminal run `heroku login`
Click open browser then accept.

Try typing `heroku` to see a list of command or `heroku apps help` to find help.

### Install Postgress addon for Heroku and it's requirements:

`pip3 install psycopg2-binary`

Use gunicorn to act as a web server

`pip3 install gunicorn`

List requirements to a file so Heroku knows what to install

`pip3 freeze --local > requirements.txt`

Create app, specifying app name:
`heroku apps:create jb-django-todo-app -- region ey`

specify `--region eu` for eu region

`git remote -v` Shows available git repositories

Therefore `git push heroku master` will push to the url displayed or `git push origin master` would push to github assuming that has been set up.

Create database addon for Heroku.

Use Heroku web gui:
Dashboard -> Project -> Resources
Addons -> Postgres -> Heroku Postgres -> Provision
Settings -> Reveal Config Vars

To connect the app to this new permanently live Postgres database:

`pip3 install dj_database_url`

This allows the connection between databases.

`pip3 freeze --local > requirements.txt`

`heroku config`

In settings.py find the database settings.

Change to:
`DATABASES = {    'default': dj_database_url.parse('')}`

Paste in the url from Heroku between the quotes within the brackets - parse('HERE!!!')

`import dj_database_url` at the top of settings.py

In terminal:
`python3 manage.py migrate`
Migrates the data to new online database




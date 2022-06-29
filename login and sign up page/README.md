**I'm available for freelance hire contact me in instagram or rabiyulfahimh@gmail.com **


Running the Project Locally

First, clone the repository to your local machine:

git clone 

https://github.com/rabiyulfahimhasim786/login--signup-django-forms.git

Now enter the directory:
```
cd mysite
```

Now create a virtual machine:
```
virtualenv venv  
source venv/bin/activate
```

Install the requirements:
```
pip install -r requirments.txt
```

Apply the migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Finally, run the development server:

```
python manage.py runserver
```

The project will be available at 127.0.0.1:8000.
License

The source code is released under the MIT License.
Conclusion

Thanks for reading this. At last Don't forget to givee a star 🌟!!

## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/


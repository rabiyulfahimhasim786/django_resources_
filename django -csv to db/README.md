<h1 style="text-align: center">DJANGO QUICK TUTORIAL COMPANION CODE</h1>

<br />
<p style="float: right;">Author: <a href="https://linktr.ee/fabriciobarbacena">Fabrício Barbacena</a></p>
<br />
<br />
https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433
## Project Description
<br />

This repository has the final version of the code I developed in my article/tutorial *[Django First Steps for Total Beginners: A Quick Tutorial](https://medium.com/towards-data-science/django-first-steps-for-the-total-beginners-a-quick-tutorial-5f1e5e7e9a8c)*, published on [Towards Data Science](https://medium.com/towards-data-science). 

The code intermediary versions are not presented here, but one can find them all in the aforementioned article, with detailed descriptions about them.

I'm putting together this present repository so that it can be used as starter code for future projects of mine. Here people will also find the route where I embed a Plotly chart on a Django page, which can be of interest for some folks out there.

<br />

## How to Install the Project
<br />

1. You need to have Python installed in your machine (3.8 or higher is recommended);

2. Create a new folder in your machine, go inside it and clone this repository. 

3. Create a virtual environment with `venv`. I called mine `.myenv`, but you can choose another name you prefer:

<span style="margin-left: 25px;">```python -m venv .myenv```</span> 

4. Activate the virtual environment. Below is the command for most Linux OS:

<span style="margin-left: 25px;">```source .myenv/bin/activate```</span>

<span style="margin-left: 25px;">Check this [Python documentation page](https://docs.python.org/3/library/venv.html) if you have doubts about the command to start your virtual environment.</span>

5. Install the required Python modules (Django, Pandas, and Plotly):

<span style="margin-left: 25px;">```pip install -r requirements.txt```</span>

<br />

## How to Use the Project
<br />

1. Run `python manage.py makemigrations` and `python manage.py migrate` to create the necessary tables in the database;

2. Start the command with `python manage.py runserver`. 8000 is the default port used by Dango;

3. On your browser, access the address http://localhost:8000;

4. Use the Links to navigate by the films pages;

5. Access http://localhost:8000/gapminder/2007 to see the most recent version of the Gapminder interactive Plotly chart.

> You can change the year in the last url to one of the available years in the Gapminder dataset from Plotly Express (1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, and 2007). Choosing a route with any other year will raise an error.

<br />

## Licence
<br />



This project is distributed under the MIT licence (see the LICENCE document).

<br/>
INTRODUCTION

So, you worked hard and developed a new modern Django web app for your client. She is very happy and congratulates you for the final result. “Great job. Now we only have to insert our millions of database rows into the new app and start using it in production”.

Some less prepared folks would froze by hearing such words, but that will not be your case: you will know how to use django-extensions and how easy it is, after you install it, to write Python scripts to quickly load data into Django databases, using Django’s ORM functionalities.

If you don’t know django-extensions yet, fear not: this quick tutorial will show how it works by presenting a very simple example. Then you can expand its use for more complex situations you may encounter in your daily activity.

PART 1: OUR MODELS AND DATA

We will use the very simplified films app I created in my Django tutorial for total beginners, published on Towards Data Science.
Django first steps for the total beginners: a quick tutorial
Learn how to embed Plotly graphs in Django apps, among other subjects

towardsdatascience.com

Its model has only two tables: films_film and films_genre. The code from films/models.py is reproduced below:

As I mentioned in my tutorial, this is not the perfect model relation between those entities, especially because it stablishes that one film cannot have more than one genre. However, I decided to build a simplified model for didactic purposes and we are going to keep it that way in the present text. If you want it, you can expand this model later, by allowing many-to-many relationships between films and genres or including new entities, such as directors and awards, for example.

The CSV file we will use can be found on my GitHub repository. It was created using data from the pixarfilms R library. Since only one genre was allowed for each film in the data model I created, I assigned the genre ‘animation’ for most of the films, but I also included some other genres, so that we didn’t have just one genre in our example.

PART 2: SETTING UP OUR ENVIRONMENT

1. Choose a folder in your machine where you want to work and clone my GitHub repository with the starter code.

git clone https://github.com/fabricius1/DjangoTutorial.git

2. Move inside the cloned folder DjangoTutorial.

cd DjangoTutorial

Notice that a pixar.csv file is already saved inside the DjangoTutorial/films folder.

3. Create a virtual environment with venv. I’m calling mine .myenv.

python -m venv .myenv

4. Activate the virtual environment by running the correct command for your chosen terminal and OS. The command below works in my Git Bash for Windows. If you have doubts about activating virtual environments with venv, please consult the Python documentation.

source .myenv/Scripts/activate

All the commands from now on must be executed with your virtual environment activated.

5. Install django and django-extensions with PIP. We will also install pandas and plotly because plotly.express is called in the films/views.py file in the cloned project.

pip install django django-extensions pandas plotly

If you want to know more about django-extensions, read the documentation, especially the page about its runscript functionality.’

6. Add the string 'django_extensions' to the list of INSTALLED_APPS in project/settings.py. Leave the other lines without change.
#
INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # films app:
    'films.apps.FilmsConfig',    # add this:
    'django_extensions',
]
#
7. Apply the migrations files to create the tables in the database:

python manage.py migrate

8. Look for errors and correct them if needed:

python manage.py check

9. Run the project locally with python manage.py runserver.

10. Check if everything is ok by opening http://localhost:8000/films on your browser and inspecting the app. No films will be displayed on the screen, since the db.sqlite3 database has just been created.
Image by Author

PART 3: CREATE AND RUN THE SCRIPT

11. Stop the server. Create a scripts folder in the project root, at the same level of manage.py:

mkdir scripts

12. Create the scripts/load_pixar.py file.

touch scripts/load_pixar.py 

13. Fill scripts/load_pixar.py with the following code. We will explain it later:

14. Run python manage.py runscript load_pixar. Please notice that load_pixar is written without the .py extension.

If everything goes fine, you will see the imported rows printed in the console.

15. Run the server again with python manage.py runserver then open http://localhost:8000/films on your browser. Check how the imported films are now displayed by this Django page:
Image by Author

PART 4: ABOUT THE SCRIPT CODE

The scripts/load_pixar.py code has only one function in it, with no dunder call at its end. As stated in the django-extensions documentation, “This file must implement a run() function. This is what gets called when you run the script. You can import any models or other parts of your Django project to use in these scripts”.

So, we import both the Films and Genre models and the csv Python builtin module in the script. Next, inside the run() function, we use the with context management structure and open the pixar.csv file by using not a relative path, but the pattern app_name/csv_file.

Then we pass the file variable to the csv.reader() function, call next(reader) to skip the CSV headers, and finally use Django’s ORM method .delete() to remove any instances that might be in the models tables. If you don’t want to delete the existing rows from the tables, remove these lines of code.

The next step is to loop over all rows in the CSV. And in this part of the code we find the important method .get_or_create() for the first time. It returns a tuple, where the object at the first index is the Django model object that was created (if it didn’t exist in the database yet) or retrieved (if it already existed). The second element in the tuple is a boolean that returns True if the object was created and False otherwise.

Notice how we create (or get) the Genre object first, and then use it, together with other information taken from every CSV row, to create a new Film object and save it to the database.

FINAL WORDS

As mentioned before, this is just a very simple example of how to use django-extensions runscript functionality. By knowing the basics, you can implement solutions to more complex models and also create code with error-handling structures, for example, to deal with exceptions.

Thank you so much, dear reader, for having honored my text with your time and attention.

Happy coding!

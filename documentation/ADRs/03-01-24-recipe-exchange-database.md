## Use a very simple recipe exchange database

As this is just for trying out how to work with the combi of Python, MariaDB and Quasar, 
and for learning to set up MariaDB.  

So I just use a single table called recipes, within the "recipes" database, consisting of:
- ID
- title
- image_url
- kcal, proteins, carbs, fats

The coach-view can write a new recipe in the DB, the trainee-view can retrieve the latest recipe and display it.

## use SQLAlchemy for MariaDB and Flask

That is the way recommended by MariaDB, they have official tutorials as well, so it seems the easiest.  
Therefore I use Python SQLAlchemy for working with MariaDB within the Flask backend. 

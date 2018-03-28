# Arcane-Server
Server code for Arcane Streaming project

## Setup
1) Make sure you have Python 3 and virtualenv installed. You can install virtualenv with:
```
$ pip install virtualenv
```

Create a virtual environment for this repository with `virtualenv <path/to/virtualenvironment>`

2) Enter the virtual env by running `source /path/to/env/bin/activate`

3) Install the dev dependancies. Run `pip3 install -r requirements(-dev).txt`

4) Create the database by running `./manage.py makemigrations` and migrate by running `./manage.py migrate`

5) Start the server by running `./manage.py runserver`. You will also need to run the client in tandem.

6) You will have to create a superuser for your local development environment with `./manage.py createsuperuser`

** Note: You will want to update the settings.py to check if it is local by adding your host name where 'Rhuarc' is.

## Pushing to Heroku
This section assumes that you have heroku [installed](https://devcenter.heroku.com/articles/heroku-cli "Heroku CLI Documentation") and logged into Arcane's heroku app, and that the heroku origin is added to git.
1) Copy over the production build of Client into the staticfiles 
2) Commit the changes
3) Run `git push heroku production:master`. This pushes the production branch up to heroku's master branch.


## Contributors
This repository was migrated over from a previous repository. Inital work was done Tyler Scott @tscott8 and Shem Sedrick @ssedrick.

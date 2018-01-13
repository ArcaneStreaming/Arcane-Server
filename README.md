# Arcane-Server
Server code for Arcane Streaming project

## Setup
1) Make sure you have Python 3 and virtualenv installed. Create a virtual env for this repository.
2) Enter the virtual env by running `source /path/to/env/bin/activate`
3) Install the dev dependancies. Run `pip install -r requirements(-dev).text`
4) Create the database by running `./manage.py makemigrations` and migrate by running `./manage.py migrate`
5) Start the server by running `./manage.py runserver`. You will also need to run the client in tandem. 
** Note: You will want to update the settings.py to check if it is local by adding your host name where 'Rhuarc' is.

## Pushing to Heroku
This section assumes that you have heroku installed and logged into Arcane's heroku app, and that the heroku origin is added to get.
1) Copy over the production build if Client into the staticfiles 
2) Run `git push heroku production:master`. This pushes the production branch up to heroku's master branch.


## Contributors
This repository was migrated over from a previous repository. Inital work was done Tyler Scott @tscott8 and Shem Sedrick @ssedrick.

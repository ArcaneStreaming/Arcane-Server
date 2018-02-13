# Arcane-Server
Server code for Arcane Streaming project

## Setup
1) Make sure you have Python 3 and virtualenv installed. You can install virtualenv with:
```
$ pip install virtualenv
```

Create a virtual environment for this repository:

```
$ virtualenv <path/to/virtualenvironment>
```

2) Enter the virtual env by running `source /path/to/env/bin/activate`

3) Install the dev dependancies. Run `pip -r requirements(-dev).text`

4) Create the database by running `./manage.py makemigrations` and migrate by running `./manage.py migrate`

5) Start the server by running `./manage.py runserver`. You will also need to run the client in tandem. 

** Note: You will want to update the settings.py to check if it is local by adding your host name where 'Rhuarc' is.

## Contributors
This repository was migrated over from a previous repository. Inital work was done Tyler Scott @tscott8 and Shem Sedrick @ssedrick.

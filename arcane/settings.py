"""
Django settings for arcane project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import socket
if socket.gethostname() == 'nickzarate.local' or socket.gethostname() == 'DESKTOP-UUOP14F':
    from .local_settings import *
else:
    from .production_settings import *

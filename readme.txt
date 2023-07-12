#terminal
pyenv local 3.11.0
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip

#terminal
pip install Django
django-admin startproject mysite .

#settings File
import os
STATIC_ROOT=os.path.join(BASE_DIR,'static')

#terminal
python3 manage.py migrate
python3 manage.py startapp app_name
python3 manage.py runserver 0.0.0.0:8000


#add to urls.py in mysite
from django.urls import path, include
path('', include('temp_stories.urls')),

#add to installed apps
'temp_stories.apps.TempStoriesConfig',


# in app folder create templates:app_name:index.html

#for POST, add https
CSRF_TRUSTED_ORIGINS = []
#goes with 
{% csrf_token %}

#for tests
python3 manage.py test
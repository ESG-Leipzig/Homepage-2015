=======================
 Setup for development
=======================

Run::

  $ virtualenv .virtualenv --python=python3
  $ source .virtualenv/bin/activate
  $ pip install -r requirements.txt
  $ npm install
  $ node_modules/.bin/bower install
  $ python manage.py migrate
  $ python manage.py createsuperuser
  $ sed -i 's/DEBUG = False/DEBUG = True/' esg_leipzig_homepage_2015_deployment/settings.py
  $ python manage.py runserver

Later run::

  $ pip install flake8==2.3.0
  $ flake8 --exclude="esg_leipzig_homepage_2015/migrations/" manage.py esg_leipzig_homepage_2015

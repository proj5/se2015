#!/bin/sh

# Clear old database
# rm db.sqlite3

# Create new database
python manage.py migrate

# Install fixture

# username:password
# admin:admin
# user:user
#python manage.py createsuperuser
python manage.py runserver

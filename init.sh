#!/bin/sh

# Clear old database
rm db.sqlite3

# Create new database
python manage.py migrate

# Install fixture

# username:password
# admin:admin
# user:user
python manage.py loaddata auth.json
python manage.py loaddata users.json
python manage.py loaddata grades.json
python manage.py loaddata skills.json
python manage.py loaddata exercises.json
python manage.py loaddata exams.json
python manage.py loaddata records.json
python manage.py loaddata possible_answer.json

# Force check pep8 when commit
gunicorn se2015.wsgi
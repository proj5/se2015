#!/bin/sh

# Clear old database
# rm db.sqlite3

# Create new database
python manage.py migrate

# Install fixture

# username:password
# admin:admin
# user:user
python manage.py loaddata auth.json
python manage.py loaddata users.json
python manage.py loaddata grades.json
python manage.py loaddata exercises.json
python manage.py loaddata skills.json
python manage.py loaddata exams.json

# Force check pep8 when commit
commit_script="#!/bin/bash
set -e
echo '---------------------------------'
pep8 --exclude=*/migrations/ .
echo '---------------------------------'
python manage.py test
"

echo "$commit_script" > .git/hooks/pre-commit
chmod 755 .git/hooks/pre-commit

@echo off
:: !Clear old database
del db.sqlite3

:: !Create new database
python manage.py migrate

:: Install fixture

:: username:password
:: admin:admin
:: user:user
python manage.py loaddata auth.json
python manage.py loaddata users.json
python manage.py loaddata grades.json
python manage.py loaddata skills.json
python manage.py loaddata exercises.json
python manage.py loaddata exams.json

:: Force check pep8 when commit
set filename=.git/hooks/pre-commit
echo #!/bin/bash >%filename%
echo set -e >>%filename%
echo echo '---------------------------------' >>%filename%
echo pep8 --exclude=*/migrations/ . >>%filename%
echo echo '---------------------------------' >>%filename%
echo python manage.py test >>%filename%



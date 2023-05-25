#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi
# python manage.py flush --noinput
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username kingship --email kingship.lc@gmail.com --noinput
# python manage.py createsuperuser --username admin --email admin@gmail.com --noinput
# python manage.py createsuperuser --username supervisor --email supervisor@gmail.com --noinput
# python manage.py createsuperuser --username user --email user@gmail.com --noinput

# python manage.py add_multiplier
# python manage.py add_dept
# python manage.py add_job_titles
# python manage.py add_fake_employees
# python manage.py add_locations
# python manage.py add_work
# python manage.py add_titles


python manage.py collectstatic --noinput

exec "$@"
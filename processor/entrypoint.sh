#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

# Create Admin user
echo "Creating admin user"
pipenv run python manage.py createsuperuser --no-input

# Start server
echo "Starting server"
echo "Starting server..."
pipenv run python manage.py runserver 0.0.0.0:8000
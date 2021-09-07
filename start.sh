#!/bin/sh -eu

python manage.py migrate
python manage.py loaddata apps/example/fixtures/example.yaml
python manage.py runserver

#!/usr/bin/env bash

TEMPLATE=https://github.com/CleitonDeLima/django-skeleton/archive/master.zip
EXTENSIONS=py,md,html,ini

echo "Enter with project name: "
read project_name


if [ -n "${project_name}" ]; then
    mkdir ${project_name}
    cd ${project_name}
    python3 -m venv .${project_name}
    source .${project_name}/bin/activate
    pip install Django==1.9.6
    django-admin.py startproject --template=${TEMPLATE} --extension=${EXTENSIONS} ${project_name}
    pip install -r requirements/development.txt
    python3 contrib/settings_gen.py
    python manage.py makemigrations thumbnail
    python manage.py migrate
fi
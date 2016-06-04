{% comment "This comment section will be deleted in the generated project" %}

## Features

* Works on Python3
* Uses Django 1.9

## The project include

* [django-extensions][2]
* [python-decouple][3]
* [dj-database-url][4]
* [dj-static][5]
* [django-libsass][6]
* [django-ckeditor][7]
* [sorl-thumbnail][8]
* [Pillow][9]
* [pytz][10]


## Quick start:

1. Run Script! :D

```sh 
curl -o temp.sh https://raw.githubusercontent.com/CleitonDeLima/django-skeleton/master/contrib/setup.sh 
&& bash ./temp.sh && rm temp.sh
```

2. Activate venv!

```sh
source .project_name/bin/activate
```



--------------------------------------------------------------------------------------------

{% endcomment %}

# {{ project_name }}

{{ project_name }} is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].


## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv {{ project_name }}`
    2. `$ . {{ project_name }}/bin/activate`

Install all dependencies:

    pip install -r requirements/development.txt

Run makemigrations and migrations:
    
    python manage.py makemigrations thumbnail
    python manage.py migrate


[0]: https://www.python.org/
[1]: https://www.djangoproject.com/

[2]: https://github.com/django-extensions/django-extensions
[3]: https://github.com/henriquebastos/python-decouple/
[4]: https://github.com/kennethreitz/dj-database-url
[5]: https://github.com/kennethreitz/dj-static
[6]: https://github.com/torchbox/django-libsass
[7]: https://github.com/django-ckeditor/django-ckeditor
[8]: https://github.com/mariocesar/sorl-thumbnail
[9]: https://github.com/python-pillow/Pillow
[10]: https://pypi.python.org/pypi/pytz?

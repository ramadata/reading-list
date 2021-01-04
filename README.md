# Programming Reading List Single Page App

A single page app of a reading list of programming books.

## Installation and Setup

To set up this project you will need these Django and a virtual environment:

1. `python3 -m pip install Django`
2. `python3 -m pip install --user virtualenv`
3. `python3 -m venv env`
4. `source env/bin/activate`

To set up a single page app you will not be using the django-admin start app command, so therefore you will need to use settings without setting the settings module. To do that follow the directions here: <https://docs.djangoproject.com/en/3.1/topics/settings/#using-settings-without-setting-django-settings-module>.

You will also need a SECRET_KEY. To generate one, use this command:

- `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

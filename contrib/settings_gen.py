#!/usr/bin/env python
from configparser import RawConfigParser


CONFIG_STRING = """
    [settings]
    DEBUG=True
    SECRET_KEY={{ secret_key }}
    ALLOWED_HOSTS=127.0.0.1, .localhost
    #DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME

    #LANGUAGE_CODE=
    #TIME_ZONE=

    #DEFAULT_FROM_EMAIL=
    EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
    #EMAIL_HOST=
    #EMAIL_PORT=
    #EMAIL_USE_TLS=
    #EMAIL_HOST_USER=
    #EMAIL_HOST_PASSWORD=
"""

config = RawConfigParser(comment_prefixes=(';',))  # 'comment_prefixes' not ignore comments
config.optionxform = lambda option: option         # keep settings uppercase
config.read_string(CONFIG_STRING)

# Writing our configuration file to 'settings.ini'
with open('../settings.ini', 'w') as configfile:
    config.write(configfile, False)
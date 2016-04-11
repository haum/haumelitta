#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# settings.py

# Settings for twitter coffee pot system

# coffeepot's master twitter name (list of unicode str)
MASTERS = [
    'jblb_72',
    'haum72',
    'matael',
    'seb_vallee',
    'MicroJoe_'
]

# pattern to start coffeepot
RE_START = 'givemecoffee'

# pattern to stop coffeepot
RE_STOP = 'thanksforcoffee'

# Time between 2 lookups for a tweet (seconds)
UPDATE_TIME = 60

# RPi commutation pin (17 -> 0)
PIN = 0

try:
    from settings_secret import *
except ImportError:
    pass

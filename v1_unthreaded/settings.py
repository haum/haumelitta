#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# settings.py

# Settings for twitter coffee pot system

# PLEASE DO NOT SHARE TOKENS


# coffee pot twitter API key
CONSUMER_KEY = 'BcNaAoasHdRJvcy1iCYw'

# coffee pot twitter api secret
CONSUMER_SECRET = 'YlHGnhc8epNPt1zlocWAWhPPCXKXp0uiW1wpoIXj1qs'

# API Token
TOKEN_KEY = '1431541796-u5b2SpNKJq4zV4vLmmj7DYVOa77Ijc9Ewexkk4r'

# Token  secret
TOKEN_SECRET = 'PPeHIZ6foEZ356sEfnKhcXajiGFoDJjNK3k7SlX94'

# coffeepot's master twitter name (list of unicode str)
MASTERS = [
    'jblb_72',
    'haum72',
    'matael',
]

# pattern to start coffeepot
RE_START = 'givemecoffee'

# pattern to stop coffeepot
RE_STOP = 'thanksforcoffee'

# Time between 2 lookups for a tweet (seconds)
UPDATE_TIME = 60

# RPi commutation pin (17 -> 0)
PIN = 0

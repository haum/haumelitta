#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# rpi_version.py
#
# Copyright © 2013 Mathieu Gaborit (matael) <mathieu@matael.org>
#
#
# Distributed under WTFPL terms
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""
Test program to link twitter and a coffee pot through a RPi.
"""

import os
import sys
import re
import time
import signal

from twitter import Twitter, OAuth
from wiringpi import pinMode, digitalWrite, wiringPiSetup

import settings

wiringPiSetup()

RE_START = re.compile(settings.RE_START)
RE_STOP = re.compile(settings.RE_STOP)


def connect_api():

    try:
        api = Twitter(
            auth=OAuth(
                settings.TOKEN_KEY,
                settings.TOKEN_SECRET,
                settings.CONSUMER_KEY,
                settings.CONSUMER_SECRET),
            api_version='1.1'
        )
        print("Connected to the twitter API")
        return api
    except Exception as e:
        print("Failed to load twitter API:")
        print(e)
        sys.exit()


def do_coffee(pin, api, last_id):
    """Must i send a signal to the coffee pot ?"""
    mention = api.statuses.mentions_timeline()[0]
    # mention = {'id_str': 'lol', 'text': 'lol', 'user': {'screen_name': 'lol'}}

    if mention['id_str'] != last_id:

        last_id = mention['id_str']
        name = mention['user']['screen_name']

        if name in settings.MASTERS:

            if RE_START.search(mention['text']):
                print("Hey ! Let's make coffee !")
                digitalWrite(pin, 0)
                return last_id

            elif RE_STOP.search(mention['text']):
                print("Yeah ! Coffee's ready !")
                digitalWrite(pin, 1)
                return last_id
    else:
        print("Waiting for a tweet...")
        return last_id


def main():

    def SIGINT_handler(sig, stack):
        """
        Handler for SIGINT
        Ensure a cleanup before exiting the program
        """

        print('Quit...')
        sys.exit()

    def SIGUSR_handler(sig, stack):
        """
        Handler for SIGUSR1 and SIGUSR2

        SIGUSR1 => switch on coffee pot
        SIGUSR2 => switch off coffee pot
        """

        if sig == signal.SIGUSR1:
            digitalWrite(pin, 0)
            print('Forced state : CoffeePot ON')
        elif sig == signal.SIGUSR2:
            digitalWrite(pin, 1)
            print('Forced state : CoffeePot OFF')

    # setup interrupt handler for SIGTERM
    signal.signal(signal.SIGINT, SIGINT_handler)
    signal.signal(signal.SIGUSR1, SIGUSR_handler)
    signal.signal(signal.SIGUSR2, SIGUSR_handler)

    # Open GPIO pin
    pin = settings.PIN
    pinMode(pin, 1)
    digitalWrite(pin, 1)

    # print instructions
    print("""
CoffeePot Controller
====================

Process ID : {0}

Commands :
----------
- SIGINT : graceful stop (with cleanup)
- SIGUSR1 : force state : coffeepot ON
- SIGUSR2 : force state : coffeepot OFF

Forcing states :
----------------

- ON : $ sudo kill -10 {0}
- OFF : $ sudo kill -12 {0}

Stop :
------

CTRL-C or $ sudo kill -2 {0}""".format(os.getpid()))

    api = connect_api()

    print("Entering main loop....")
    last_id = '0'
    while 1:
        time.sleep(settings.UPDATE_TIME)
        last_id = do_coffee(pin, api, last_id)
        print('Updating...')
    return 0


if __name__ == '__main__':
    main()

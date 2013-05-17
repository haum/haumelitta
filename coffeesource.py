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

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Ok, you should run this shitty script as root.")

import os
import sys
import re
import twitter
import time
import signal

from sig_handlers import *
from settings import *
RE_START = re.compile(RE_START)
RE_STOP = re.compile(RE_STOP)

def setup_gpio():
    """ Setup function """

    # use the P1.17 as the out pin (default to LOW)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW)


def do_coffee(api, last_id):
    """Must i send a signal to the coffee pot ?"""
    mention = api.GetMentions()[:1]


    if mention[0].id != last_id:

        last_id  = mention[0].id
        name = mention[0].user._screen_name

        if name in MASTERS:

            if RE_START.search(mention[0].text):
                print("Hey ! Let's make coffee !")
                GPIO.output(17, GPIO.HIGH)
                return last_id

            elif RE_STOP.search(mention[0].text):
                print("Yeah ! Coffee's ready !")
                GPIO.output(17, GPIO.LOW)
                return last_id
    else:
        print("Waiting for a tweet...")
        return last_id


def main():
    # setup interrupt handler for SIGTERM
    signal.signal(signal.SIGINT, SIGINT_handler)
    signal.signal(signal.SIGUSR1, SIGUSR_handler)
    signal.signal(signal.SIGUSR2, SIGUSR_handler)

    # let's create an instance of the api
    try:
        api = twitter.Api(consumer_key=CONSUMER_KEY,\
                          consumer_secret=CONSUMER_SECRET,\
                          access_token_key=TOKEN_KEY,\
                          access_token_secret=TOKEN_SECRET)
        print("Connected to the twitter API")
    except:
        print("Failed to load twitter API")
        sys.exit()

    setup_gpio()

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


    print("Entering main loop....")
    last_id = 0
    while 1:
        last_id = do_coffee(api, last_id)
        time.sleep(UPDATE_TIME)
    return 0

if __name__=='__main__':main()

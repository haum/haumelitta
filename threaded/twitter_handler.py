#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# twitter_handler.py
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
Twitter handler thread for HAUMelitta
"""

import threading
import time
import logging
import sys
import re

from twitter import Twitter, OAuth

from globals import *
from settings import *

class TwitterHandler(threading.Thread):
    """
    Twitter handler
    """

    def __init__(self):
        """ Constructor """

        threading.Thread.__init__(self)

        # initialize API or die.
        try:
            self.api = Twitter(
                auth=OAuth(TOKEN_KEY, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET),
                api_version='1.1'
            )
            logging.info("Twitter > Connected to Twitter API")
        except:
            logging.critical("Twitter > Failed to load twitter API")
            sys.exit()

        # compile regexps
        self.RE_START = re.compile(RE_START)
        self.RE_STOP = re.compile(RE_STOP)

        # init needed vars
        self.last_id = "0"

    def run(self):
        """
        On run, this thread enters in a inifinite polling loop, steps are :

            1. check if twitter polling's enabled
            2. check for new mentions
            3. parse last mention and if its ID is different from last_id, proceed
            4. check if mention is for one of the masters and contains one of the keywords
            5. process accordingly

        """

        while True:

            mention = self.api.statuses.mentions_timeline()[0]

            if mention['id_str'] != self.last_id:

                self.last_id  = mention['id_str']
                name = mention['user']['screen_name']

                if name in MASTERS:

                    if self.RE_START.search(mention['text']):
                        with LK_commutable:
                            logging.info("Twitter > Hey ! Let's make coffee !")
                            CoffeePin.Instance().pin.value = 1

                    elif self.RE_STOP.search(mention['text']):
                        with LK_commutable:
                            logging.info("Twitter > Yeah ! Coffee's ready !")
                            CoffeePin.Instance().pin.value = 0
            else:
                logging.info("Twitter > Waiting for a tweet...")

            time.sleep(5*60)


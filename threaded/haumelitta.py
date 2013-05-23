#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# haumelitta.py
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
Threaded version of HAUMelitta's control script.
"""

import signal

import quick2wire.gpio as gpio

from settings import *
from globals import *
from twitter_handler import TwitterHandler
from sig_handlers import *


def main():
    """ main program """

    # Open GPIO pin
    with LK_commutable:
        coffee_pin = gpio.pins.pin(PIN, direction=gpio.Out)
        coffee_pin.open()

    # setup interrupt handler for SIGINT
    # setup forced state signals
    signal.signal(signal.SIGINT, SIGINT_handler)
    signal.signal(signal.SIGUSR1, SIGUSR_handler)
    signal.signal(signal.SIGUSR2, SIGUSR_handler)

    # init. twitter thread and start it
    twitter_thread = TwitterHandler()
    twitter_thread.start()


if __name__=='__main__': main()

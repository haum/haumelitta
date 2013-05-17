#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# sig_handlers.py
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
Signal handlers.

SIGINT_handler : Graceful stop
SIGUSR_handler : Forced states
"""

import sys
import signal
import quick2wire.gpio as gpio
from settings import *

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

    if sig==signal.SIGUSR1:
        with gpio.pins.pin(PIN, direction=gpio.Out) as p:
            p.value = 1
        print('Forced state : CoffeePot ON')
    elif sig==signal.SIGUSR2:
        with gpio.pins.pin(PIN, direction=gpio.Out) as p:
            p.value = 0
        print('Forced state : CoffeePot OFF')





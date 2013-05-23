#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# globals.py
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
Global variable....


I know, globals are terrible things that we all shall fear...

But, you know, here, globals are related to physical I/O pin that won't vanish, or locks.
It's really lighter to use global here instead of a singleton for example....
"""

import threading
from singleton import Singleton

@Singleton
class CoffeePin:

    def __init__(self):
        self.pin = 0

# gpio.pins.Pin to coffeepot
global coffee_pin
coffee_pin = CoffeePin()

# can we commute the pin
global LK_commutable
LK_commutable = threading.Lock()



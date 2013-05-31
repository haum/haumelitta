#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# coffeepot_control.py
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
Functions to control coffeepot
"""

import quick2wire.gpio as gpio

from settings import COFFEE_PIN

def activate():
    """ Activate the coffee pot """
    try:
        with gpio.pins.pin(COFFEE_PIN, direction=gpio.Out) as p:
            p.value = 1
        return 0
    except:
        return 1


def desactivate():
    """ Desctivate the coffee pot """
    try:
        with gpio.pins.pin(COFFEE_PIN, direction=gpio.Out) as p:
            p.value = 0
        return 0
    except:
        return 1

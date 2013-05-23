#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# gpio_handler.py
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
GPIO handler for HAUMelitta
"""

import select
import threading

import quick2wire.i2c as i2c
import quick2wire.gpio as gpio

from globals import *
from settings import *

I2C_ADDR = 0x38         # adresse of PCF8574 8-BIT I/O EXPANDER

class GPIOHandler(threading.Thread):
    """ GPIO Handler thread

    Physical interface to force coffeepot's state
    """

    def __init__(self):
        """ Constructor """

        # setup port expander
        # writing 0xFF sets all lines as input
        # logical 1 appears when a line is driven to ground
        with i2c.I2CMaster() as bus:
            bus.transaction(
                i2c.writing_bytes(I2C_ADDR, 0xFF))

        # setup interrupt signal
        self.int = gpio.pins.Pin(I2C_INT, direction=In, interrupt=Rising)

        self.poller = select.epoll()
        # setup pin as a readable and edge triggered
        self.poller.register(self.int, select.POLLIN | select.POLLET)


    def run(self):
        """ Check for an event on GPIO 4 and handle it """

        with self.int:
            while True:
                events = self.poller.poll()

                for fno,ev in events:
                    if fno == self.pin.fileno():
                        self.handle_i2c_interrupt()

    def handle_i2c_interrupt(self):
        """ Called on interruption after a change on I2C expander
        This function reads all I2C port to find what changed
        """
        with i2c.I2CMaster() as bus:
            #read values from IO expander
            read_results = bus.transaction(i2c.reading(address, 1))
            IOexp_results = read_results[0][0]
            print("%02x" % IOexp_results)


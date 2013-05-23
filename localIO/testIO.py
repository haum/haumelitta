#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# testIO.py
#
# Copyright © 2013 jerome breheret (@jlbl_72) jerome@jblb.no-ip.com
#
#
# Distributed under WTFPL terms
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
# 0. You just DO WHAT THE FUCK YOU WANT TO.
#

"""
Test program to use I2C io on  a RPi.
"""

import select
import quick2wire.i2c as i2c	# import Quick2Wire I2C API

address = 0x38			# adresse of PCF8574 8-BIT I/O EXPANDER

# set IO as input: write 1 to coresponding IO pin; 0xFF for all input
with i2c.I2CMaster() as bus:
	bus.transaction(
		i2c.writing_bytes(address, 0xFF))

while True:
	with i2c.I2CMaster() as bus:
	#read values from IO expander
		read_results = bus.transaction(
				i2c.reading(address, 1))

		IOexp_results = read_results[0][0]
		print("%02x" % IOexp_results)


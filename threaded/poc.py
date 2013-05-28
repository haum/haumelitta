#! /usr/bin/env python
# -*- coding:utf8 -*-
#

import quick2wire.i2c as i2c
import quick2wire.gpio as gpio
import select

I2C_ADDR = 0x38			# adresse of PCF8574 8-BIT I/O EXPANDER
I2C_INT =  7			# pin 7 handle I2C interupt

def handle_i2c_interrupt():
		""" Called on interruption after a change on I2C expander
		This function reads all I2C port to find what changed
		"""
		with i2c.I2CMaster() as bus:
			#read values from IO expander
			read_results = bus.transaction(i2c.reading(I2C_ADDR, 1))
			IOexp_results = read_results[0][0]
			print("%02x" % IOexp_results)

def main():
	""" main program """
	# setup I2C port expander
	# writing 0xFF sets all lines as input
	# logical 0 appears when a line is driven to ground
	# INTERUPT pin is driving to ground where IO pin change
	with i2c.I2CMaster() as bus:
		bus.transaction(
		i2c.writing_bytes(I2C_ADDR, 0xFF))

		# setup interrupt signal
	interupt = gpio.pins.pin(I2C_INT, direction=gpio.In, interrupt=gpio.Rising)
	interupt.open()

	epoller1 = select.epoll()
	# setup pin as a readable and edge triggered
	epoller1.register(interupt, select.EPOLLIN | select.EPOLLET) # EPOLLIN & EPOLLET Edge for python3

	while True:
		events = epoller1.poll()

		for fno,ev in events:
			if fno == interupt.fileno():
				handle_i2c_interrupt()

if __name__=='__main__': main()

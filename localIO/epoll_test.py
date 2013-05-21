#! /usr/bin/env python3

import sys
from quick2wire.gpio import Pin
import select

pin_num = int(sys.argv[1]) if len(sys.argv) > 1 else 12

# Trigger should be one of "none", "rising", "falling", or "both"
trigger = str.strip(sys.argv[2]) if len(sys.argv) > 2 else Pin.Both

pin = Pin(pin_num, Pin.In, trigger)

ep = select.epoll()
ep.register(pin, select.EPOLLET | select.EPOLLIN)
ep.register(sys.stdin.fileno(), select.EPOLLIN)

while True:
    print("Waiting on pin", pin, "with edge trigger", trigger)
    events = ep.poll()
    for fileno, event in events:
        if fileno == sys.stdin.fileno():
            sys.exit()
        if event & select.EPOLLIN:
            print("ready for reading, value is ", pin.value)
        if event & select.EPOLLOUT:
            print("ready for writing")
        if event & select.EPOLLERR:
            print("error signaled while polling")



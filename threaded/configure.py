#! /usr/bin/env python
# -*- coding:utf8 -*-
#
#
# read config from file, create if not exist
#
# ref of value needed http://pads.haum.org/p/haumelitta_settings

import os

if not os.path.exists("./setting.py"):
    with open('./setting.py', 'w') as f:
        f.write('#! /usr/bin/env python\n')
        f.write('# -*- coding:utf8 -*-\n')
        f.write('#\n\n')
try:
        from setting import TOKEN_KEY
except ImportError:
        TOKEN_KEY = raw_input('twitter TOKEN_KEY: ')
        with open('./setting.py', 'a') as f:
            f.write("TOKEN_KEY = \'" + TOKEN_KEY + "\'\n\n" )

try:
        from setting import TOKEN_SECRET
except ImportError:
        TOKEN_SECRET = raw_input('twitter TOKEN_SECRET: ')
        with open('./setting.py', 'a') as f:
            f.write("TOKEN_SECRET = \'" + TOKEN_SECRET + "\'\n\n" )

try:
        from setting import CONSUMER_KEY
except ImportError:
        CONSUMER_KEY = raw_input('twitter CONSUMER_KEY: ')
        with open('./setting.py', 'a') as f:
            f.write("CONSUMER_KEY = \'" + CONSUMER_KEY + "\'\n\n" )

try:
        from setting import CONSUMER_SECRET
except ImportError:
        CONSUMER_SECRET = raw_input('twitter CONSUMER_SECRET: ')
        with open('./setting.py', 'a') as f:
            f.write("CONSUMER_SECRET = \'" + CONSUMER_SECRET + "\'\n\n" )


try:
        from setting import COFFEE_PIN
except ImportError:
        COFFEE_PIN = raw_input('COFFEE_PIN: ')
        with open('./setting.py', 'a') as f:
            f.write("COFFEE_PIN = " + COFFEE_PIN + "\n" )

try:
        from setting import I2C_ADDR
except ImportError:
        I2C_ADDR = raw_input('I2C_ADDR: ')
        with open('./setting.py', 'a') as f:
            f.write("I2C_ADDR = " + I2C_ADDR + "\n" )

try:
        from setting import I2C_INT
except ImportError:
        I2C_INT = raw_input('I2C_INT: ')
        with open('./setting.py', 'a') as f:
            f.write("I2C_INT = " + I2C_INT + "\n" )

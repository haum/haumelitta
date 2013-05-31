#! /usr/bin/env python
# -*- coding:utf8 -*-
#

import os

#if os.path.exists("./setting.py"):
#	from settings import *


	try:
		from setting import *
    except IOError:
    """
        le reste fonction creation setting
# twitter
    TOKEN_KEY
    TOKEN_SECRET
    CONSUMER_KEY
    CONSUMER_SECRET
# GPIO
    COFFEE_PIN
    I2C_ADDR
    I2C_INT
 
 delete any setting file   
 ask TOKEN_KEY
 add TOKEN_KEY to file
 ask TOKEN_SECRET
 add TOKEN_SECRET to file
 """

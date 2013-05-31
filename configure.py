#! /usr/bin/env python
# -*- coding:utf8 -*-
#

import os

#if os.path.exists("./setting.py"):
#	from settings import *


	try:
		from setting import *
    except IOError:
        le reste fonction creation setting

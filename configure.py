#! /usr/bin/env python
# -*- coding:utf8 -*-
#

import os

if os.path.exists("./setting.py"):
	from settings import *


""" try:
        import setting
    except IOError:
        le reste fonction creation setting

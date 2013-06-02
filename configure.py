#! /usr/bin/env python
# -*- coding:utf8 -*-
#

import os

#if not os.path.exists("./setting.py"):
#		f = open("./setting.py",'w')
#		f.write('#! /usr/bin/env python\n')
#		f.write('# -*- coding:utf8 -*-\n')
#		f.write('#\n\n')
#try:
#		from setting import TOKEN_KEY
#except ImportError:
#		
#		TOKEN_KEY = raw_input('twitter TOKEN_KEY: ')
#		f.write("TOKEN_KEY = \'" + TOKEN_KEY + "\'\n" )



try:
   	from setting import *
except ImportError:
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
	"""
# delete any setting file   
if os.path.exists("./setting.py"):
	os.remove("./setting.py")

# open file for write
f = open("./setting.py",'w')
f.write('#! /usr/bin/env python\n')
f.write('# -*- coding:utf8 -*-\n')
f.write('#\n\n')
TOKEN_KEY = raw_input('twitter TOKEN_KEY: ')
f.write("TOKEN_KEY = \'" + TOKEN_KEY + "\'\n" )



# ask TOKEN_KEY
# add TOKEN_KEY to file
# ask TOKEN_SECRET
# add TOKEN_SECRET to file


f.close()

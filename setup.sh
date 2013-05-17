#! /bin/bash
#
# rpi_setup.sh
# Author: Matael

# Setup python package for tweeting coffeePot

# update distribute (RPi.GPIO requires last version)
easy_install3 -U distribute

# because it's *much* better
easy_install3 -U pip

pip-3.2 install twitter

echo "This script will upgrade/install : distribute, pip, twitter, RPi.GPIO"



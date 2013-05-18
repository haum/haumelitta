HAUMelitta
==========

HAUMelitta is a project intended to connect a coffeepot to the Internet through a Twitter account.

It our modest contribution to the Web of object.

Why this name ?
---------------

The name in contraction of HAUM (our hackerspace) and Melitta (well-known coffepot manufacturer).

How does it works ?
-------------------

The coffeepot has its own Twitter account (@HAUMelitta) and API tokens/secrets had been generated to get updates on the
Pi.

When a tweet containing the right keyword is emitted from one of the masters, the Pi commutes a static relay that switch
on the coffeepot.

Requirements
------------

Here's what you need...

### Bill of material

- A RaspberryPi (tested on raspbian)
- A Coffeepot
- A static relay

### Software part

You'll need several python modules, just grab the `setup.sh` script and run :

    $ sudo su
    # sudo apt-get install python3
    # ./setup.sh

Modules are :

- `quick2wire`
- `twitter`

To setup the `quick2wire` module, follow the steps described [here](https://github.com/quick2wire/quick2wire-python-api).

Running
-------

Connect your static relay to commute on pin 17 (port 1 on Pi).

Run :

    $ sudo python coffeesource.py

Control instructions will be written in the console.



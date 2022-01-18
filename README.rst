Python API for Hisense Televisions
##################################

A fork built to support the `Homebridge-Hisense-TV`_.

CLI Usage
*********
::

    usage: hisensetv [-h] [--authorize] [--get {sources,volume}]
                     [--key {back,down,exit,left,menu,power,right,up}] [--no-ssl] [-v]
                     hostname --ifname <name>

    Hisense TV control.

    positional arguments:
      hostname              Hostname or IP for the TV.
      
    required arguments:
      --ifname              Name of the network interface to use to connect to the TV (eg. eth0)

    optional arguments:
      -h, --help            show this help message and exit
      --authorize           Authorize this API to access the TV.
      --get {sources,volume}
                            Gets a value from the TV.
      --key {back,down,exit,left,menu,power,right,up}
                            Sends a keypress to the TV.
      --no-ssl              Do not connect with SSL (required for some models).
      -v, --verbose         Logging verbosity.

One Time Setup
==============
**Note:** This is not required for all models!

::

    hisensetv 10.0.0.128 --authorize   
    Please enter the 4-digit code: 7815

Keypresses
==========
::

    hisensetv 10.0.0.28 --key up
    [2020-02-29 13:48:52,064] [INFO    ] sending keypress: up

Gets
====
::

    hisensetv 10.0.0.28 --get volume
    [2020-02-29 13:49:00,800] [INFO    ] volume: {
        "volume_type": 0,
        "volume_value": 1
    }

.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
.. |Build Status| image:: https://api.travis-ci.com/newAM/hisensetv.svg?branch=master
   :target: https://travis-ci.com/newAM/hisensetv
.. |PyPi Version| image:: https://img.shields.io/pypi/v/hisensetv
    :target: https://pypi.org/project/hisensetv/
.. |docs| image:: https://readthedocs.org/projects/hisensetv/badge/?version=latest
   :target: https://hisensetv.readthedocs.io/en/latest/?badge=latest
.. _mqtt-hisensetv: https://github.com/Krazy998/mqtt-hisensetv
.. _455: https://github.com/eclipse/paho.mqtt.python/issues/455
.. _Homebridge-Hisense-TV: https://github.com/MrAsterisco/homebridge-hisense-tv

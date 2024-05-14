Python API for Hisense Televisions
##################################

A MQTT service to interact with HiSense TVs.

This fork provides support for the `Homebridge-Hisense-TV`_ and it is not available as separate distribution.

Dependencies
==============

- Python 3.8 or later.
- paho-mqtt 1.5.0 or higher.
- netifaces 0.11.0 or higher.

CLI Usage
==============

::

    usage: hisensetv.py [-h] [--authorize] [--ifname IFNAME]
                    [--get {sources,volume,state}]
                    [--key {power,up,down,left,right,menu,back,exit,ok,volume_up,volume_down,channel_up,channel_down,fast_forward,rewind,stop,play,pause,mute,home,subtitle,netflix,youtube,amazon,0,1,2,3,4,5,6,7,8,9,source_0,source_1,source_2,source_3,source_4,source_5,source_6,source_7}]
                    [--no-ssl] [--certfile CERTFILE] [--keyfile KEYFILE] [-v]
                    hostname

    Hisense TV control.

    positional arguments:
        hostname              Hostname or IP for the TV.

    optional arguments:
      -h, --help            show this help message and exit
      --authorize           Authorize this API to access the TV.
      --ifname IFNAME       Name of the network interface to use
      --get {sources,volume,state}
                            Gets a value from the TV.
      --key {power,up,down,left,right,menu,back,exit,ok,volume_up,volume_down,channel_up,channel_down,fast_forward,rewind,stop,play,pause,mute,home,subtitle,netflix,youtube,amazon,0,1,2,3,4,5,6,7,8,9,source_0,source_1,source_2,source_3,source_4,source_5,source_6,source_7}
                            Sends a keypress to the TV.
      --no-ssl              Do not connect with SSL (required for some models).
      --certfile CERTFILE   Absolute path to the .cer file (required for some
                            models). Works only when --keyfile is also specified.
                            Will be ignored if --no-ssl is specified.
      --keyfile KEYFILE     Absolute path to the .pkcs8 file (required for some
                            models). Works only when --certfile is also specified.
                            Will be ignored if --no-ssl is specified.
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

#!/usr/bin/env python

# diffusion - the text language diff engine for baobao
#
# copyright (c) 2015 - jorge valdez
# javaldez@smu.edu
#
# created for the engaged learning project with Alex Saladna (asaladna@smu.edu)
#
# feedme/__init__.py - initialization file
#   sets the __all__ variable and preps the files for direct import

# allows you to do the following:
#   from feedme import Cleanr 
from cleanr import Cleanr
from speakr import Speakr

# when you import *, this is where you set what all gets imported
__all__ = ['cleanr.py', 'speakr.py']

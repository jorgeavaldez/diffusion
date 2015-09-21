#!/usr/bin/env python

# diffusion - the text language diff engine for baobao
#
# copyright (c) 2015 - jorge valdez
# javaldez@smu.edu
#
# created for the engaged learning project with Alex Saladna (asaladna@smu.edu)
#
# llama - nlp and translation engine
#   uses the pattern library and different translation apis to translate the
#   text blurbs, diff them, and determine accuracy

import json
import sys

# this is the import for the parse tagging api
# it imports the english version of the parser, but there are versions for
#   spanish - es
#   french - fr
#   italian - it
#   german - de
#   dutch - nl
from pattern.en import parse

class Llama(object):

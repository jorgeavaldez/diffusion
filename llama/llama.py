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
from pattern.en import parse as parse_en
from pattern.en import parsetree as parsetree_en

from pattern.es import parse as parse_es
from pattern.es import parsetree as parsetree_es

class Llama(object):
    def __init__(self):
        '''Constructor.'''

    def tokenize_text(self, txt):
        '''Tokenizes the given text. Returns '''

    def gen_parse_tree_en(self, txt):
        '''Generates a parse tree from english text.'''
        
        txt_tree = parsetree_en(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def gen_parse_tree_es(self, txt):
        '''Generates a parse tree from spanish text.'''
        
        txt_tree = parsetree_es(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

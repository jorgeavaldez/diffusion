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

from collections import OrderedDict
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

from pattern.fr import parse as parse_fr
from pattern.fr import parsetree as parsetree_fr

from pattern.de import parse as parse_de
from pattern.de import parsetree as parsetree_de

from pattern.it import parse as parse_it
from pattern.it import parsetree as parsetree_it

from pattern.nl import parse as parse_nl
from pattern.nl import parsetree as parsetree_nl

# for the heavy duty nlp stuff
from pattern.vector import Document, Model

class Llama(object):
    def __init__(self, txt):
        '''Constructor.'''
        self.txt = txt

    def text_frequencies(self, ptree, chunkType=True, chunkRole=True,
        wordType=True, wordF=True):
        '''Calculates the appropriate frequencies of the word and chunk types
        within the given parse tree and outputs as a dict of dicts.'''

        # So the parse tree is returned as a list of Sentences, each of which is
        # made up of Chunks that are made up of Words. Here we traverse this madness
        # to format for output.
        if chunkType:
            chunkTypeFreq = {}
        
        if chunkRole:
            chunkRoleFreq = {}

        if wordType:
            wordTypeFreq = {}

        if wordF:
            wordFreq = {}

        for s in ptree:
            for ch in s.chunks:
                # Chunk type frequencies
                if chunkType and str(ch.type) in chunkTypeFreq.keys():
                    chunkTypeFreq[str(ch.type)] += 1

                elif chunkType:
                    chunkTypeFreq[str(ch.type)] = 1

                # Chunk role frequencies
                if chunkRole and str(ch.role) in chunkRoleFreq.keys():
                    chunkRoleFreq[str(ch.role)] += 1

                elif chunkRole:
                    chunkRoleFreq[str(ch.role)] = 1

                for w in ch:
                    # Word frequencies
                    if wordF and w.string.encode('utf-8') in wordFreq.keys():
                        wordFreq[w.string.encode('utf-8')] += 1

                    elif wordF:
                         wordFreq[w.string.encode('utf-8')] = 1

                    # Word type frequencies
                    if wordType and w.type in wordTypeFreq.keys():
                        wordTypeFreq[w.type] += 1

                    elif wordType:
                        wordTypeFreq[w.type] = 1

        # This is gonna be the response.
        # The only other way would be to use a tuple but those are ghetto af.
        res = {}

        # Sort the bitches
        if chunkType:
            chunkTypeFreq = OrderedDict(sorted(chunkTypeFreq.items(),
                 key=lambda x: x[1], reverse=True))
            res['chunkTypeFreq'] = chunkTypeFreq

        if chunkRole:
            chunkRoleFreq = OrderedDict(sorted(chunkRoleFreq.items(),
                key=lambda x: x[1], reverse=True))
            res['chunkRoleFreq'] = chunkRoleFreq

        if wordF:
            wordFreq = OrderedDict(sorted(wordFreq.items(),
                key=lambda x: x[1], reverse=True))
            res['wordFreq'] = wordFreq

        if wordType:
            wordTypeFreq = OrderedDict(sorted(wordTypeFreq.items(),
                key=lambda x: x[1], reverse=True))
            res['wordTypeFreq'] = wordTypeFreq

        return res

    def doc_vector(self, txt):
        '''Generates a document from the input text, and calculates the tf-idf
        and various statistics from the pattern vector module.'''
        doc = Document(txt, 

    def gen_parse_tree_en(self, txt=self.txt):
        '''Generates a parse tree from english text.'''

        txt_tree = parsetree_en(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def gen_parse_tree_es(self, txt=self.txt):
        '''Generates a parse tree from spanish text.'''

        txt_tree = parsetree_es(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def gen_parse_tree_fr(self, txt=self.txt):
        '''Generates a parse tree from french text.'''

        txt_tree = parsetree_fr(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def gen_parse_tree_de(self, txt=self.txt):
        '''Generates a parse tree from german text.'''

        txt_tree = parsetree_de(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def gen_parse_tree_it(self, txt=self.txt):
        '''Generates a parse tree from italian text.'''

        txt_tree = parsetree_it(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def gen_parse_tree_nl(self, txt=self.txt):
        '''Generates a parse tree from dutch text.'''

        txt_tree = parsetree_nl(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

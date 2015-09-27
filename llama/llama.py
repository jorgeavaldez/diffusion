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
from pattern.vector import Document, Model, stem, LEMMA

class Llama(object):
    def __init__(self, txt, lang='en'):
        '''Constructor.'''
        self.txt = txt
        self.lang = lang
        self.ptree = self.gen_parse_tree()
        self.doc_raw = Document(txt, stopwords=True)
        self.doc = Document(txt, stemmer=LEMMA, stopwords=False)

    def ptree_frequencies(self, ptree=None, chunkType=True, chunkRole=True,
        wordType=True):
        '''Calculates the appropriate frequencies of the word and chunk types
        within the given parse tree and outputs as a dict of dicts.'''

        if ptree is None:
            ptree = self.ptree

        # So the parse tree is returned as a list of Sentences, each of which is
        # made up of Chunks that are made up of Words. Here we traverse this madness
        # to format for output.
        if chunkType:
            chunkTypeFreq = {}
        
        if chunkRole:
            chunkRoleFreq = {}

        if wordType:
            wordTypeFreq = {}

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

        if wordType:
            wordTypeFreq = OrderedDict(sorted(wordTypeFreq.items(),
                key=lambda x: x[1], reverse=True))
            res['wordTypeFreq'] = wordTypeFreq

        return res

    def doc_vector_frequencies(self, doc=None):
        '''Generates a document from the input text, and calculates the tf-idf
        and various statistics from the pattern vector module.'''

        if doc is None:
            doc = self.doc
        
    def gen_parse_tree(self, txt=None, lang=None):
        '''Returns the parsetree for the given language. The language defaults
        to this Llamas language.'''

        if txt is None:
            txt = self.txt

        if lang is None:
            lang = self.lang

        if lang == 'en':
            return self._gen_parse_tree_en(txt)

        elif lang == 'es':
            return self._gen_parse_tree_es(txt)

        elif lang == 'fr':
            return self._gen_parse_tree_fr(txt)
        
        elif lang == 'de':
            return self._gen_parse_tree_de(txt)

        elif lang == 'it':
            return self._gen_parse_tree_it(txt)

        elif lang == 'nl':
            return self._gen_parse_tree_fr(txt)

    # parse tree generators for each language.
    # don't use this, use gen_parse_tree instead.

    def _gen_parse_tree_en(self, txt=None):
        '''Generates a parse tree from english text.'''
        
        if txt is None:
            txt = self.txt

        txt_tree = parsetree_en(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def _gen_parse_tree_es(self, txt=None):
        '''Generates a parse tree from spanish text.'''

        if txt is None:
            txt = self.txt

        txt_tree = parsetree_es(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def _gen_parse_tree_fr(self, txt=None):
        '''Generates a parse tree from french text.'''

        if txt is None:
            txt = self.txt

        txt_tree = parsetree_fr(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def _gen_parse_tree_de(self, txt=None):
        '''Generates a parse tree from german text.'''

        if txt is None:
            txt = self.txt

        txt_tree = parsetree_de(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def _gen_parse_tree_it(self, txt=None):
        '''Generates a parse tree from italian text.'''

        if txt is None:
            txt = self.txt

        txt_tree = parsetree_it(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

    def _gen_parse_tree_nl(self, txt=None):
        '''Generates a parse tree from dutch text.'''

        if txt is None:
            txt = self.txt

        txt_tree = parsetree_nl(txt, tokenize=True, tags=True, chunks=True,
                relations=True, lemmata=True, encoding='utf-8')

        return txt_tree

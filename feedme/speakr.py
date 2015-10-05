#!/usr/bin/env python

# diffusion - the text language diff engine for baobao
# 
# copyright (c) 2015 - jorge valdez
# javaldez@smu.edu
#
# created for the engaged learning project with Alex Saladna (asaladna@smu.edu)
#
# feedme/Speakr - feed translation library
#   uses the google translate api to translate text
#   api key is set as an environment variable, $GOOGLE_API_KEY

import re
import requests
import sys
import json
import os

class Speakr(object):
    def __init__(self):
        '''Constructur.'''

        self.base_url = 'https://www.googleapis.com/language/translate/v2'

        self.google_t_api_key = os.environ['GOOGLE_API_KEY']

        self.google_t_payload = {}

    def _set_get_req_payload(self, chunk, s_lang, t_lang, *args):
        '''Sets the internal payload that gets sent along with the
        request function. The necessary parameters are the chunk of text to
        translate, the destination language, and the target language. Extra
        parameters are expected as a dictionary with appropriate key-value
        pairs. '''
        if not url:
            return

        # The source and target languages must be in the format of the language
        # codes found at:
        # https://cloud.google.com/translate/v2/using_rest#language-params
        #
        # A description for each of the request parameters can be found here:
        # https://cloud.google.com/translate/v2/using_rest#query-params

        self.google_t_payload = { 'format' : 'text',
                                  'key' : self.google_t_api_key,
                                  'q' : chunk,
                                  'source' : s_lang,
                                  'target' : t_lang }

        if args:
            for k in args.keys():
                self.google_t_payload[k] = args[k]

    def translate_text_google(self, chunk, s_lang, t_lang):
        '''Pulls and article and runs it throught the readability api. Encodes
        in utf-8 to allow for multiple languages, and also cleans through
        beautiful soup to remove tags.'''
        if not self.google_t_payload:
            self._set_get_req_payload(chunk, s_lang, t_lang)

        res = requests.get(self.base_url, params=self.google_t_payload)

        res_obj = json.loads(res.text.encode('utf-8'))

        # the key here comes from what we want out of the readability json
        # response
        bsoup_dump = BeautifulSoup(res_obj['content'], 'html.parser')

        return bsoup_dump.get_text().encode('utf-8').strip()

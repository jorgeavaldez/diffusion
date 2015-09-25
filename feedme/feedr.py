#!/usr/bin/env python

# diffusion - the text language diff engine for baobao
# 
# copyright (c) 2015 - jorge valdez
# javaldez@smu.edu
#
# created for the engaged learning project with Alex Saladna (asaladna@smu.edu)
#
# feed_me - feed cleaning and text parsing library
#   uses the readability api to extract text from web urls
#   api key is kept in the same directory as readability_key.txt

import re
import requests
import sys
import json
import os

from bs4 import BeautifulSoup

class Feedr(object):
    def __init__(self):
        '''Constructor. Instantiates the base_url and opens the api key and loads
        it into memory.'''

        self.base_url = 'http://readability.com/api/content/v1/parser'

        self.r_api_key = os.environ['READABILITY_KEY']

        self.r_payload = {}
            
    def _set_get_req_payload(self, url, *args):
        '''Sets the internal payload that gets sent along with the
        request function. The only necessary parameter is the url, extra
        parameters are expected as a dictionary with appropriate key-value
        pairs. '''
        if not url:
            return

        self.r_payload = {'token' : self.r_api_key, 'url' : url}

        if args:
            for k in args.keys():
                self.r_payload[k] = args[k]
        
    def readability_web_process(self, url):
        '''Pulls and article and runs it throught the readability api. Encodes
        in utf-8 to allow for multiple languages, and also cleans through
        beautiful soup to remove tags.'''
        if not self.r_payload:
            self._set_get_req_payload(url)

        res = requests.get(self.base_url, params=self.r_payload)

        res_obj = json.loads(res.text.encode('utf-8'))

        # the key here comes from what we want out of the readability json
        # response
        bsoup_dump = BeautifulSoup(res_obj['content'], 'html.parser')

        return bsoup_dump.get_text().encode('utf-8').strip()

def main():
    url = raw_input('url: ')
    f = Feedr()

    res = f.readability_web_process(url)
    print(res)

if __name__ == "__main__":
    main()

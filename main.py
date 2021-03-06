#!/usr/bin/env python

from feedme import Cleanr, Speakr
from llama import Llama

import matplotlib.pyplot as plt
import numpy as np

from collections import OrderedDict
import time

def llama_test_out(lma):
    # We're sticking the parse tree in an output file because there's too much
    # to print normally.
    sample_out_file = open('main_out/' + time.strftime('%m%d%Y%H%M%S') +
            '_' + str(lang) + '_' + 'sample_out.txt', 'w')

    # We're gonna use the llama text freq function here
    freqDicts = lma.ptree_frequencies()

    # So the parse tree is returned as a list of Sentences, each of which is
    # made up of Chunks that are made up of Words. Here we traverse this madness
    # to format for output.
    chunkTypeFreq = freqDicts['chunkTypeFreq']
    chunkRoleFreq = freqDicts['chunkRoleFreq']
    wordTypeFreq = freqDicts['wordTypeFreq']

    # We need to pull the dicts from llama
    sample_out_file.write("CHUNK TYPE\n")

    for t in chunkTypeFreq.keys():
        sample_out_file.write(str(t) + ": " + str(chunkTypeFreq[t]))
        sample_out_file.write("\n")

    sample_out_file.write("\nCHUNK ROLE\n")

    for t in chunkRoleFreq.keys():
        sample_out_file.write(str(t) + ": " + str(chunkRoleFreq[t]))
        sample_out_file.write("\n")

    sample_out_file.write("\nWORD TYPE FREQUENCIES\n")

    for t in wordTypeFreq.keys():
        sample_out_file.write(str(t) + ": " + str(wordTypeFreq[t]))
        sample_out_file.write("\n")

    sample_out_file.close()

def speakr_test_out(txt):
    spkr = Speakr()

    spkr.translate_text_google(txt), 

def main():
    lang = raw_input('lang: ')
    url = raw_input('url: ')

    # The Cleanr object consumes the url and is our interface with the
    # Readability API
    f = Cleanr()
    response = f.readability_web_process(url)

    out_txt_res = open('clean_article_out.txt', 'w')
    out_txt_res.write(response)
    out_txt_res.close()

    # Because LLAMAS
    lma = Llama(response, lang)

    llama_test_out(lma)

if __name__ == "__main__":
    main()

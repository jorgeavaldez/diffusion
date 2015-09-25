#!/usr/bin/env python

from feedme import Feedr
from llama import Llama

def main():
    url = raw_input('url: ')

    # The Feedr object consumes the url and is our interface with the
    # Readability API
    f = Feedr()

    response = f.readability_web_process(url)

    print('CLEAN TEXT\n=======================')
    print(response)
    print('\n')
    print('PARSE TREE\n=======================')

    # Because LLAMA'S
    lma = Llama()
    ptree = lma.gen_parse_tree_en(response)

    # We're sticking the parse tree in an output file because there's too much
    # to print normally.
    sample_out_file = open('s_out.txt', 'w')

    # So the parse tree is returned as a list of Sentences, each of which is
    # made up of Chunks that are made up of Words. Here we traverse this madness
    # to format for output.
    for s in ptree:
        for ch in s.chunks:
            # Just some of the different properties that we can display from a
            # chunk
            sample_out_file.write(str(ch.type) + " " + str(ch.role) + " " + 
                    str([(w.string.encode('utf-8'), w.type) for w in ch]) + "\n")

    sample_out_file.close()
    
if __name__ == "__main__":
    main()

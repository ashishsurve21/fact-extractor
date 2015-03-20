#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import shutil
import sys


DEBUG = True

"""
loading wiki page ids for the articles of soccer
    @filein <type 'str'> file name 
    @return <type 'str'> list of soccer player page ids
"""
def load_wiki_ids(filein):
    with open(filein) as i:
        return [l.strip() for l in i.readlines()]

"""
    Extracting articles for soccer from the wiki articles dump
    @soccer_ids <type 'object'>    soccer player ids which are to be extracted from the wiki articles
    @corpus_dir    <type 'str'>    path of the directory where the wiki articles are store
    @output_dir    <type 'str'>    path of the directory where soccer player output will be stored
"""
def extract_soccer_articles(soccer_ids, corpus_dir, output_dir):
    for path, subdirs, files in os.walk(corpus_dir):
        for name in files:
            f = os.path.join(path, name)
            with open(f) as i:
                content = ''.join(i.readlines())
            match = re.search('id="([^"]+)"', content)
            current_id = match.group(1)
            if DEBUG:
                print "File = [%s] - Wiki ID = [%s]" % (f, current_id)
            if current_id in soccer_ids:
                shutil.copy(f, output_dir)
                if DEBUG:
                    print "MATCHED! [%s]" % content
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Usage: %s <SOCCER_IDS> <CORPUS_DIR> <OUTPUT_DIR>" % __file__
        sys.exit(1)
    else:
        ids = load_wiki_ids(sys.argv[1])
        extract_soccer_articles(ids, sys.argv[2], sys.argv[3])

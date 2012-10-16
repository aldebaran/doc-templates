#! /usr/sbin/env python

import os
import sys

path = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(path))

def main(root):
    import qiapidoc.datas.indexparser
    parser = qiapidoc.datas.indexparser.IndexParser(root)
    parser.parse_index()
    print parser.objs

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit('usage: {} xml_root'.format(sys.argv[0]))
    main(sys.argv[1])

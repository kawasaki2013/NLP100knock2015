#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/05/27 16:40:28 Shin Kanouchi

import argparse
import knock030


def main(doc):
    for sent in doc:
        for m in sent:
            if m['pos'] == '動詞':
                print m['surface']

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/neko.mecab', help='input training data')
    args = parser.parse_args()
    my_morphs = knock030.get_morphs(args.train)
    main(my_morphs)

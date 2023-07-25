# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import nltk
import stanza

if __name__ == '__main__':
    nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')
    stanza.download('en', package='mimic', processors={'ner': 'i2b2'}, verbose=False)

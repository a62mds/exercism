# -*- encoding: utf-8 -*-
#!/usr/bin/env python
import re


def word_count(sentence):
    word_re = re.compile(ur'[^\W_]+', re.UNICODE)
    # sentence.decode('utf-8') necessary for use w/ Python 2.7
    words = [word.lower()for word in word_re.findall(sentence.decode('utf-8'))]
    return {word : words.count(word) for word in set(words)}

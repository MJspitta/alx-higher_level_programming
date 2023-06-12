#!/usr/bin/python3
def multiple_returns(sentence):
    s_len = len(sentence)
    if s_len == 0:
        s_first = None
    else:
        s_first = sentence[0]
    return s_len, s_first

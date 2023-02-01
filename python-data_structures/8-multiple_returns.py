#!/usr/bin/python3
def multiple_returns(sentence):
    # sentence = "At school, I learnt C!"
    if sentence:
        length = len(sentence)
    else:
        length = None
    first = sentence[0]
    return length, first

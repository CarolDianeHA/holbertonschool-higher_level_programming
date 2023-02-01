#!/usr/bin/python3
def multiple_returns(sentence):
    # sentence = "At school, I learnt C!"
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return 0, None

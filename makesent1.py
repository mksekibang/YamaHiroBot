#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import MeCab

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result

def makesent(text):
    if __name__ == "__main__":
        wordlist = wakati(text)

        # Create table of Markov Chain
        markov = {}
        w1 = ""
        for word in wordlist:
            if w1:
                if w1 not in markov:
                    markov[w1] = []
                markov[w1].append(word)
            w1 = word

        # Generate Sentence
        count = 0
        sentence = ""
        w1  = random.choice(markov.keys())
        while count < len(wordlist):
            tmp = random.choice(markov[w1])
            sentence += tmp
            w1 = tmp
            count += 1
            if len(sentence) > 280:
                break
        sentence = sentence[0:sentence.rfind("。")]
        return sentence

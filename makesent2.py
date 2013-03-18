#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import MeCab

def wakati(text):
    t = MeCab.Tagger("-Owakati")
    m = t.parse(text)
    result = m.rstrip(" \n").split(" ")
    return result

def makesent():
    try:
        filename = "text.txt"
        src = open(filename, "r").read()
        wordlist = wakati(src)
        # Create table of Markov Chain
        markov = {}
        w1 = ""
        w2 = ""
        for word in wordlist:
            if w1 and w2:
                if (w1, w2) not in markov:
                    markov[(w1, w2)] = []
                markov[(w1, w2)].append(word)
            w1, w2 = w2, word

        # Generate Sentence
        count = 0
        sentence = ""
        w1, w2  = random.choice(markov.keys())
        while count < len(wordlist):
            tmp = random.choice(markov[(w1, w2)])
            sentence += tmp
            w1, w2 = w2, tmp
            count += 1
            if len(sentence) > 280:
                break
        return sentence
    except:
        return "Error"

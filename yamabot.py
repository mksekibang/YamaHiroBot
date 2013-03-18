#! /usr/local/bin/python
# coding: utf-8
##
## hiroo bot main
##
import htmlread
import htmlget
import random
import time
import os
import re
import katakakkodel

accCnt = 0
neta = open("yamabot.txt","w")
netaCnt = 0
while netaCnt <= 50:
    w = open("text.txt","w")
    crowl = random.uniform(2,5)
    _crowl = 0
    while crowl >= _crowl:
        urlList = open("AccList.text","r").read()
        urlList = urlList.split("\n")
        html = htmlget.htmlget(random.choice(urlList))
        text = str(htmlread.htmlread(html))
        w.write("\n" + text)
        _crowl += 1
        accCnt += 1
        time.sleep(3)
        if accCnt % 50 == 0:
            print accCnt
    w.close()
    if crowl % 2 == 0:
        import makesent2
        sentence = makesent2.makesent()
    else:
        import makesent3
        sentence = makesent3.makesent()
    if sentence <> "Error":
        ##テキストの最終調整
        #変な文字は削除
        mstr = unicode("[0-9]|[一-龠]|[ぁ-ん]|[a-zA-Z]|[ァ-ヴ]|[！・ー。、？!?]")
        sentence = re.findall(mstr,unicode(sentence))
        #読点などで文章を終えるよう調整
        mstr = unicode("[0-9一-龠ぁ-んa-zA-Zァ-ヴ]+[！。？!?]")
        sentence = re.findall(mstr,"".join(sentence))
        sentence = katakakkodel.rm_parentheses("".join(sentence))
        sentence = sentence.encode("utf-8")
        if sentence <> "":
            if netaCnt == 0:
                neta.write(sentence)
            else:
                neta.write("\n" + sentence)
            neta.flush()
            netaCnt += 1
    os.remove("text.txt")
    time.sleep(5)
neta.close()

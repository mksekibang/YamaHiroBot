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
accCnt = 0
##w = open("text.txt","w")
crowl = random.uniform(2,5)
_crowl = 0
##while crowl >= _crowl:
##    urlList = open("AccList.text","r").read()
##    urlList = urlList.split("\n")
##    a = random.choice(urlList)
##    print a
##    html = htmlget.htmlget(a)
##    text = str(htmlread.htmlread(html))
##    w.write("\n" + str(text))
##    _crowl += 1
##    accCnt += 1
##    time.sleep(3)
##w.close()
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
    sentenceB = re.findall(mstr,unicode(sentence))
    mstr = unicode("[0-9一-龠ぁ-んa-zA-Zァ-ヴ]+[！。？!?]")
    sentence = re.findall(mstr,"".join(sentenceB))
    import katakakkodel
    sentence = katakakkodel.rm_parentheses(unicode("".join(sentence)))
print sentence.encode("utf-8")

#!/usr/bin/python
# -*- encoding: utf-8 -*-

def rm_parentheses(txt=u""):
    #print txt
    import re
    pr = re.compile(ur'\{|\(|\[|\「|\［|\【|\『|\｛|\〔|“|‘|《|\
                      \}|\)|\]|\」|\］|\】|\』|\｝|\〕|”|’|》')
    parentheses = {u"『":u"』",  # left
                   u"{":u"}",
                   u"(":u")",
                   u"【":u"】",
                   u"〔":u"〕",
                   u"[":u"］",
                   u"｛":u"｝",
                   u"「":u"」",
                   u"“":u"”",
                   u'"':u'"',
                   u'《':u'》',
                   u"』":u"『",  # right
                   u"}":u"{",
                   u"」":u"「",
                   u")":u"(",
                   u"】":u"【",
                   u"〕":u"〔",
                   u"］":u"[",
                   u"｝":u"｛",
                   u"”":u"“",
                   u"》":u"《"}


    #文字列から文字を一つずつ取り出す
    for m in txt:
        #print m,
        #対象の括弧が見つかったら
        if pr.match(m):
            #parenthesesを利用して、相手の括弧を見つけ、oppositeに入れる
            opposite = parentheses[m]
            #print opposite
            try:
                #相手が見つからなければその括弧は削除する
                if re.search(opposite, txt) == None:
                    txt = re.sub(m, "", txt)
                #エラーは無視
            except re.error:
                pass
    return txt

if __name__ == '__main__':
    print rm_parentheses(u"(あいうえお)「きゃー！！")

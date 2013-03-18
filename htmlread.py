#! /usr/local/bin/python
# coding: utf-8
## Plain Text Maiker
## http://www.panopticon.jp/blog/2007/11/182337.html
##
import BeautifulSoup
import re

def getNavigableStrings(soup):
  if isinstance(soup, BeautifulSoup.NavigableString):
    if type(soup) not in (BeautifulSoup.Comment,
      BeautifulSoup.Declaration) and soup.strip():
      yield soup
  elif soup.name not in ('script', 'style'):
    for c in soup.contents:
      for g in getNavigableStrings(c):
        yield g
def htmlread(html):
  buf = html.read()
  soup = BeautifulSoup.BeautifulSoup(buf)
  text = '\n'.join(getNavigableStrings(soup))
## 文章整形いろいろ
  text = text.replace(" ","")
  text = text.replace("\n","")
  text = text.replace("xmlversion='1.0'encoding='%SOUP-ENCODING%'","")
  text = text.replace("YAMAGATAHiroo&lt;hiyori13@alum.mit.edu&gt;","")
  text = text.replace("YAMAGATA Hiroo<hiyori13@alum.mit.edu>","")
  text = text.replace("YAMAGATAHiroo(hiyori13@alum.mit.edu)","")
  ## 日付＋IDを削除
  text = re.sub(r"(\()+(.)+(id)(\))","",text)
  ## 英語だけのものは削除
  text = re.sub(r"[a-zA-Z]{10,}","",text)
  text = re.sub(r"(-){5,}","",text)
  text = re.sub(r"(&lt;)+[a-z/.:]+(&gt;)","",text)
  text = re.sub(ur"山形日本語トップ","",text)
  text = re.sub(ur"YAMAGATAHirooトップ","",text)
  text = re.sub(ur"YAMAGATAHiroo日本語トップへ","",text)
  return text

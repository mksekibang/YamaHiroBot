#! /usr/local/bin/python
# coding: utf-8
import urllib2

def htmlget(url):
    try:
    ## Only if you use Proxy, follow proccess is need
        ## Set your ID & Password
        passmgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passmgr.add_password(None,"http://1.1.179.155:8080","59807478","xdr5xsw2")
        authinfo = urllib2.ProxyBasicAuthHandler(passmgr)
        proxy_support = urllib2.ProxyHandler({"http" : "http://1.1.179.155:8080"})

        opener = urllib2.build_opener(proxy_support, authinfo)
        urllib2.install_opener(opener)
    ##
        f = urllib2.urlopen(url)
        return f
    except urllib2.HTTPError:
        print(url)
        print("HTTPError")
    except urllib2.URLError:
        print("URL Not Found")



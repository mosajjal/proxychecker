import urllib2, socket
from sys import argv


ProxyType = "http"
TestURL = "http://www.google.com"

socket.setdefaulttimeout(180)


# read the list of proxy IPs in proxyList from the first Argument given
script, filename = argv
proxylistfile = open(filename)
proxyList = proxylistfile.read().splitlines()

def is_bad_proxy(ipport):    
    try:        
        proxy_handler = urllib2.ProxyHandler({ProxyType: ipport})        
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)        
        req=urllib2.Request(TestURL)
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:        
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

        print "ERROR:", detail
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print "Bad Proxy", item
    else:
        print "working" , item

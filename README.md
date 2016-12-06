# ProxyChecker
A (very) Simple Proxy checking tool written in Python3


# Usage:

Create a file in the same directory as checker.py, fill it with ip:port (one line each), like this:

* 127.0.0.1:8888
* 192.168.1.1:8080
* PROXY:PORT  

Save it (e.g. list.txt), then call the script like this:

  $ python checker.py list.txt

For you Tor lovers, we can do all these behind tor proxy. First install PySocks (`pip install pysocks`), then add these BEFORE THE FIRST LINE:

```python
import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
```
NOTE: Remove `socket` from the original first line as well. 

Simple enough,right? 

# Notes:

1. For now, only HTTP(S? test and tell me) proxies are supported.
2. You can change the test URL to whatever you want in the script

# proxychecker
A (very) Simple Proxy checking tool written in Python3


# Usage:

Create a file in the same directory as checker.py, fill it with ip:port (one line each), like this:

* 127.0.0.1:8888
* 192.168.1.1:8080
  

Save it (e.g. list.txt), then call the script like this:

  $ python checker.py list.txt

Simple enough,right? 

# Notes:

1. For now, only HTTP proxies are supported.
2. You can change the test URL to whatever you want in the script

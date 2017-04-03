# ProxyChecker

A Simple Proxy checking tool written in Python3.

# Requirements

Python 3.5 or higher
aiohttp

# Usage:

Create a file in the same directory as checker.py, fill it with ip:port (one line each), like this:

* 127.0.0.1:8888
* 192.168.1.1:8080
* PROXY:PORT  

Save it (e.g. list.txt), then call the script like this:

  $ python3 checker.py list.txt


# Notes:

1. For now, only HTTP proxies are supported.
2. You can change the test URL to whatever you want in the script
3. This script uses `asyncio` and does the tests in parallel mode.
4. This proxy uses "via" header option to test if the URL is a valid Proxy.
import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
#!/usr/bin/env python3

import socket 

# In this challenge, send a POST request to /pentesterlab with the body of the request containing: <key><value>please</value></key> and the header Content-Type set to application/xml

host = 'ptl-822fd027-be476a53.libcurl.so'
port = 80

body = "<key><value>please</value></key>"
conLen = len(bytes(body,'utf-8'))

headers = "POST /pentesterlab HTTP/1.1\r\n"
headers += "Host: ptl-822fd027-be476a53.libcurl.so\r\n"
headers += "Content-Type: application/xml\r\n"
headers += f"Content-Length: {conLen}\r\n"
headers += "Connection: close\r\n"
headers += "\r\n"

payload = bytes(headers,'utf-8') + bytes(body,'utf-8')
print(payload.decode())

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

s.sendall(payload)
while True:
    data = s.recv(1024)
    if not data:
        break

    print(data.decode())


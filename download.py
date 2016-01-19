#!/usr/bin/env python

import socket as sk 
#import os

def mkDownloadRequest(serv, objNmae):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}" + "\r\n\r\n").format(o=objNmae, s=serv)


#print "{!r".format(mkDownloadRequest('intranet.mahidol', '/'))

servName = 'www.images6.fanpop.com'
#http://images6.fanpop.com/image/photos/37100000/Lovely-Nala_Cat-nala-the-cat-37155814-701-701.jpg
#'intranet.mahidol'
port = 80


## create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

##connect to a destinatio  as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, '/image/photos/37100000/Lovely-Nala_Cat-nala-the-cat-37155814-701-701.jpg')  #'/'
sock.send(request)

while True:
	data = sock.recv(1024)
	#start_i = data.find('Content-Length')   #cut behind \r\n\r\n
	f = open('new.txt', "w")
	f.write(data)
	end_i = data.find('\r\n\r\n')
	length = int((((data[start_i:end_i]).split(":"))[1])[1:]) #find content-length
	f.write("\nlength is " + str(length))
	count = len(data[end_i+4:]) ## /r =1 /n =1
	while count < length :   ## why it not stop when i set it to <=
		data = sock.recv(1024)
		f.write(data)
		count += len(data)
	f.write("\nContent-Length is " + str(length))
	f.write("\nCount value is " + str(count))
	#if len(data)==0:
	sock.close()
	break
	


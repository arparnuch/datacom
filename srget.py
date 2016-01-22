#!/usr/bin/env python

import socket as sk 
import os

def mkDownloadRequest(serv, objNmae):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}" + "\r\n\r\n").format(o=objNmae, s=serv)


def getheader(sock__): ## index is the index of \r\n\r\n ## if the web does not have header this function is DOOMED
	while True:
		data = sock__.recv(1024)
		text = ""
		text = text + data
		found_index = text.find('\r\n\r\n')
		header_length = 0
		header_length += len(data)
		if found_index != -1: ## found \r\n\r\n
			header = data[:found_index]
		
		piece = data[found_index+4:]
		break

	if not os.path.exists('./header.txt'): # if not exisit create file
		f3 = open('./header.txt', "w")
	with open('header.txt', "w") as f:
		f.write(header)

	# print header
	# print "=============================================="
	# print piece
	# print header_length
	return (header, piece, header_length)

def getcontenlength(header): ## get header file
	count = 0
	enter_index = 0
	content_length_index = header.find('Content-Length')
	# print content_length_index
	boo_found_CL = False
	content_length = 0

	if content_length_index != -1:
		enter_index = header[content_length_index:].find('\r\n')
		content_length = header[content_length_index:content_length_index + enter_index].split(':')[1][1:]
		boo_found_CL = True
		# print content_length

	return int(content_length)


def check_file():
	if not os.path.exists('./data.txt'): # if not exisit create file
		f4 = open('./data.txt', "w")






servName = 'www.google.co.th'
#'classroomclipart.com'
#
#'intranet.mahidol'
port = 80


## create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

##connect to a destinatio  as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, '/')  #'/'
sock.send(request)

def download_file(sock__):
	check_file() ## how to use with open('./header.txt', './data.txt', "rw") as f1, f2
	
	while True:
		header_info = getheader(sock__) 
		header = header_info[0]
		piece = header_info[1]
		header_length = header_info[2]
		content_length = getcontenlength(header)
		
		body = ""
		body_length = 0
		body += piece
		body_length += len(piece)
		
		if body_length == content_length:
			pass
		else:
			data = sock__.recv(1024)
			body += data

		if content_length == 0:  ## DEAL WITH "not found conten_length in the header"
			## load until last data == None --> end
			while len(data) != 0:
				body_length += len(data)
				body += data

		else:
			while body_length < content_length:
				body_length += len(data)
				body += data

		with open('./data.txt', "w") as f:
			f.write(body)
		
		sock__.close()
		break		


# getheader(sock)
download_file(sock)

#print "{!r".format(mkDownloadRequest('intranet.mahidol', '/'))











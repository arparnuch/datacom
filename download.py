#!/usr/bin/env python

import socket as sk 
import os

def mkDownloadRequest(serv, objNmae):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}" + "\r\n\r\n").format(o=objNmae, s=serv)


def getheader(data): ## index is the index of \r\n\r\n
	while True:
		# data = sock__.recv(1024)
		text = ""
		text = text + data
		found_index = text.find('\r\n\r\n')
		header_length = 0
		header_length += len(data)
		if found_index != -1: ## found \r\n\r\n
			header = data[:found_index]
		
		piece = data[found_index+5:]
		break

	print header
	# print "=============================================="
	# print piece
	# print header_length
	return (header, piece, header_length)

def getcontenlength(header): ## get header file
	count = 0
	enter_count = 0
	content_length_index = header.find('Content-Length')
	
	if content_length_index != -1:
		enter_count = header.find('\r\n')
		if enter_count != -1: ## found \r\n
			count += 1
			if count == 1:
				content_length = header[content_length_index:content_length_index+enter_count+1].split(':')[1][1:]
				print content_length

	return content_length

#print "{!r".format(mkDownloadRequest('intranet.mahidol', '/'))
def download_file(sock__):
	while True:
		data = sock__.recv(1024)
		boo_not_found_2enter = True
		piece = ""
		header = ""
		header_length = 0
		## if found \r\n\r\n in data then stop sending data to get header  // send data until found \r\n\r\n
		while boo_not_found_2enter:

			header_info = getheader(data) ## write to another file
			header = header[0]
			piece = header_info[1]
			header_length = header_info[2]
			if data.find('\r\n\r\n') != -1: ## Stop this loop if found \r\n\r\n
				boo_not_found_2enter = False

		content_length = getcontenlength(header)
		# print "Something"
		if !boo_not_found_2enter:  ## after we found \r\n\r\n

			# !!!!!!!!! body_length = 0 - header_length + piece  ## start keep body length to compare with content-length and body data itself
			body_length += len(data)
			#with open() as f:

			## write body data to file ----- and start to check if bodylength < content_length


			
		sock__.close()
		break		









servName = 'classroomclipart.com'
#'www.google.com'
#'intranet.mahidol'
port = 80


## create an empty socket
sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

##connect to a destinatio  as specified by the pair
sock.connect((servName, port))

request = mkDownloadRequest(servName, '/')  #'/'
sock.send(request)

if not os.path.exists('./header.txt'):
	f3 = open('./header.txt', "w")
	
if not os.path.exists('./info.txt'):
	f4 = open('./info.txt', "w")

# header, piece = getheader(sock)
# getcontenlength(header)
download_file(sock)


# with open('./info.txt', "rw") as f1:
# 	while True:
# 		data = sock.recv(1024)

# 		# header_length = 0
# 		# body_length = 0
# 		# end_count = 0

# 		getheader(sock)
# 		# if end_count <=1: ## count the header length
# 		# 	header_length += len(data)
# 		# 	print header_length
	
# 		# f1.write(data)
# 		# end_index = f1.read().find('\r\n\r\n')
# 		# if end_index != -1: 
# 		# 	end_count += 1  # use end_count for found \r\n\r\n


# 		# if end_count == 1: ## find \r\n\r\n first time
# 		# 	getcontenlength(f1) 
# 		# 	getheader()
# 		# 	body_length += data[end_index+5:]
			

		

# 	# while count < length :   ## why it not stop when i set it to <=
# 	#  	data = sock.recv(1024)
# 	#  	body_length += len(data)


# 		sock.close()
# 		break
	










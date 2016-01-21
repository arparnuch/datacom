#!/usr/bin/env python

import socket as sk 
import os

def mkDownloadRequest(serv, objNmae):
	return ("GET {o} HTTP/1.1\r\n" + "Host: {s}" + "\r\n\r\n").format(o=objNmae, s=serv)


def getheader(sock__): ## index is the index of \r\n\r\n
	while True:
		data = sock__.recv(1024)
		text = ""
		text = text + data
		found_index = text.find('\r\n\r\n')

		if found_index != -1: ## found \r\n\r\n
			header = data[:found_index]
		
		piece = data[found_index+5:]
		break

	print header
	# print "=============================================="
	# print piece
	return (header, piece)

def getcontenlength(header): ## get header file
	count = 0
	enter_count = 0
	content_length_index = header.find('Content-Length')
	# print content_length_index

	if content_length_index != -1:
		enter_count = header.find('\r\n')
		# print enter_count
		# print enter_count
		if enter_count != -1: ## found \r\n
			count += 1
			# print "enter"
			if count == 1:
				length = header[content_length_index:content_length_index+enter_count+1].split(':')[1][1:]
				print length

	# return length

#print "{!r".format(mkDownloadRequest('intranet.mahidol', '/'))
def download_file(sock__, header, piece):
	while True:
		data = sock__.recv(1024)

		## if found \r\n\r\n in data then stop sending data to get header

		body_length = 0 - getcontenlength(header) + len(piece)
		body_length += len(data)


servName = 'www.google.com'
#http://images6.fanpop.com/image/photos/37100000/Lovely-Nala_Cat-nala-the-cat-37155814-701-701.jpg
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

header, piece = getheader(sock)
getcontenlength(header)
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
			

		

# 	## if we can find the end of header --> int count content-length
	
# 	# while count < length :   ## why it not stop when i set it to <=
# 	#  	data = sock.recv(1024)
# 	#  	body_length += len(data)


# 		sock.close()
# 		break
	



# 	## if found \r\n\r\n --> slice header from 0 to found_index


# ## cut from 0:found index







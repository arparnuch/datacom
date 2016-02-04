# datacom

Usage:  srget -o <output file> -c <numConn> http://someurl.domain[:port]/path/to/file

An example: 

if you want to download a picture in www.website.com or http://www.website.com with 2 connection named as filename.jpg
-->  srget -o filename.jpg -c 2 www.website.com

Download a file from the given url with given number of connection
Name output file -o <filename> 
		** filename include file extension
Download with number of connection -c <number of connection> 

Used Library:
	asyncore
	socket 
	from cStringIO import StringIO ## StringIO append is faster than the normal one
	os
	sys
	urlparse 
	
*Note:	[example: www.website.com/folder/.../filename.file_extension]
	serv = host = www.website.com
	objName = path = /folder/.../filename.file_extension
	start = start download at start index
	end = end load file at end index
	HEADER : all neccessary information of the given URL ex. size and modified date of the given URL, etc.
	result : URL filtered from urlparse (import) into list of neccessary information
Helper Function:

	mkRangeRequest(serv, objNmae, start, end)
		: recieve all the argument to create http request for download file from start index to end index

	getHeaderRequest(serv, objNmae)
		: make a request to server so that the server sends only HEADER of the given URL

	extact_header(data)
		: it will get a chunk of data sent from the beginning of the file to the chunk that '\r\n\r\n' which indicate as the end of header and write only HEADER in the file name: 'header.txt' and send (if there is any not) header data to the main function

	getHeader_Before(result)
		: This function will open new connection and extract servName and path from result, so that we can use it to form a request to the server.
			* This function only use when a file resume [extract the neccesary data that will let the program know if the file is modified or not]

	getcontenlength(header)
		: extract only content length [file size in byte unit] 

	getSomething(filename, something)
		: return something
checkResumable(oldfile, newfile, downloaded_size)

Class:

class HTTPClient(asyncore.dispatcher)

Main Function:

main()



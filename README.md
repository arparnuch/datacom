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
	something : can only be "ETag" or "Last-Modified"
	oldfile: file contain old header that get when download file for the first time 
	newfile: file contained new header get from given URL when resume file 

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
		: return something extracted from the filename which is the header text file

	checkResumable(oldfile, newfile, downloaded_size)
		: extract "content length", "ETag", "Last-Modifie" from the both old and new header from oldfile and newfile so that we can compare them to check if the downloading file is the same file or not [modified]. It will return boolean. If boolean is true mean it is the same file 
		(continue the resumed path. However, if return false --> go to [re-]downlod the whole file)
Class:

	class HTTPClient:
		this class will retrieve host, path, port, filename, start, end from the main function and it will send host, path, port, start and end to send http request to the server from start index to end index and write downloaded file named as filename

Main Function:

	main():
		1.	acquire content length from the getHeader_Before function before to check if the header contain content length or not.
			If not include content length--> download[or re-download] the whole file.
		2.	If include content length --> check the next step in the filename already exist or not
			If not --> download[or re-download] the whole file.
		3.	checkResumable function if this file is the same file or not. [check content-length , ETag, Last-Modifie]
			If not the same file [modified] --> download[or re-download] the whole file.
			If it is the same file --> resume from start_index = downloaded index to the end of file from the given data.



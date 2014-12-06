#!/usr/bin/env python

import socket
import re
import time
import psycopg2

# Standard socket stuff:
host = ''  # do we need socket.gethostname() ?
port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # don't queue up any requests

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024)  # get the request, 1kB max
    # Look in the first line of the request for an avatoken
    # A token request should be e.g. 'http://server/?avatoken=alphanum64'

    match = re.search('GET /\?avatoken=(.{7}) HTTP/1', req, re.IGNORECASE)
    if match:
        token = match.group(1)
        
	#pull out UserAgent as well
	useragent = re.search('^User-Agent: (.+)$',req, re.MULTILINE | re.IGNORECASE).group(1)
	 
	#output = str(req.replace("\n","").replace("\r","\t"))
	
	dbwrite(token, useragent)

        #with open("ava_log_file.txt", "a") as logfile:
            #logfile.write(str(time.time()) + ","+angle+","+output+"\n")
            #logfile.close()
        print "\nToken received: " + token + ", " + useragent + " \n"
        csock.sendall("""HTTP/1.0 200 OK
Content-Type: text/html

<html>
<head>
<title>Success</title>
</head>
<body>
Golly darn and dang dabbit
</body>
</html>
""")
    else:
        # If there was no recognised command then return a 404 (page not found)
        print "Returning 404"
        csock.sendall("HTTP/1.0 404 Not Found\r\n")
    
csock.close()

def dbwrite(token, useragent):
	dbname="ava"
	dbuser="ava"
	dbpass="algernon"

	conn = psycopg2.connect(database=dbname, user=dbuser, password=dbpass)
	cur = conn.cursor()

	cur.execute(
    		"insert into TABLENAME (token, ua) values (%s, %s)",
		(token, useragent))

	conn.commit()
	cur.close
	conn.close()



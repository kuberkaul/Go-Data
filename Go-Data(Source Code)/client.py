# simpleClient6a.py
# A client to go along with simpleApp6.py
# Just lets you login and logout,
# and also get the IP address of someone else
# who is logged in (only useful if you are on the same LAN).
# As with the accompanying server, this is overly simplistic
# with little/no security.  This is only for demonstrational purposes!
import os
import urllib
import urllib2
import cookielib
import re
import getpass
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import cache2
import sys

#SERVER = "http://localhost:8080/client"
SERVER = "http://godatacloud.appspot.com/client"

import socket
users_email_address = raw_input("Enter your Gmail email address:")
users_password      = getpass.getpass()

target_authenticated_google_app_engine_uri = 'http://godatacloud.appspot.com/client'
my_app_name = "godatacloud"



# we use a cookie to authenticate with Google App Engine
#  by registering a cookie handler here, this will automatically store the 
#  cookie returned when we use urllib2 to open http://currentcost.appspot.com/_ah/login
cookiejar = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
urllib2.install_opener(opener)

#
# get an AuthToken from Google accounts
#
auth_uri = 'https://www.google.com/accounts/ClientLogin'
authreq_data = urllib.urlencode({ "Email":   users_email_address,
                                  "Passwd":  users_password,
                                  "service": "ah",
                                  "source":  my_app_name,
                                  "accountType": "HOSTED_OR_GOOGLE" })
auth_req = urllib2.Request(auth_uri, data=authreq_data)
auth_resp = urllib2.urlopen(auth_req)
auth_resp_body = auth_resp.read()
# auth response includes several fields - we're interested in 
#  the bit after Auth= 
auth_resp_dict = dict(x.split("=")
                      for x in auth_resp_body.split("\n") if x)
authtoken = auth_resp_dict["Auth"]

#
# get a cookie
# 
#  the call to request a cookie will also automatically redirect us to the page
#   that we want to go to
#  the cookie jar will automatically provide the cookie when we reach the 
#   redirected location

# this is where I actually want to go to
serv_uri = target_authenticated_google_app_engine_uri

serv_args = {}
serv_args['continue'] = serv_uri
serv_args['auth']     = authtoken

full_serv_uri = "http://godatacloud.appspot.com/_ah/login?%s" % (urllib.urlencode(serv_args))

serv_req = urllib2.Request(full_serv_uri)
serv_resp = urllib2.urlopen(serv_req)
serv_resp_body = serv_resp.read()

# serv_resp_body should contain the contents of the 
#  target_authenticated_google_app_engine_uri page - as we will have been 
#  redirected to that page automatically 
#
# to prove this, I'm just gonna print it out
#print serv_resp_body


def doCmd(cmdArgs):
    fileinformation=[]
    upload_url=""
    fid=""
    filename=""
    #http://localhost:8080/?cmd=getIP&user=wilma&pwd=def&targetUser=wilma
    url = SERVER+"?"
    url += "&".join(["%s=%s"%(arg,cmdArgs[arg]) for arg in cmdArgs])
    #print url
    response = urllib2.urlopen(url)
    #print response
    html = response.read()
    #print html
    #print html
    argu=[(arg,cmdArgs[arg]) for arg in cmdArgs]
    #print argu
    if argu[0][1]=='getFile':
	for line in html.split("\n"):
		#print line
		m=re.search(r'<td>(.*)</td><td>(.*)</td>',line)
		if m:
			fid=m.group(2)
			filename=m.group(1)
			#print upload_url
	return (fid,filename)	
	
    if argu[0][1]=='upload':
	for line in html.split("\n"):
		#print line
		m=re.search(r'<td>(.*)</td><td>(.*)</td>',line)
		if m:
			upload_url=m.group(2)
			#print upload_url
	return upload_url	
	
    for line in html.split("\n"):
	m=re.search(r'<td>(.*)</td><td>(.*)</td>',line)

	if m:
		fileinformation.append(m.group(1)+":"+m.group(2))
    return fileinformation


def main():

    FileInfo={}
    FileInfo['Filename']=[]
    FileInfo['Size']=[]
    FileInfo['User']=[]
    FileInfo['Time']=[]
    FileInfo['ContentType']=[]
    register_openers()
    if (sys.argv[1]=="view"):
	f=doCmd({"cmd":"view"})
    	for i in f:
		FileInfo[i.split(":")[0]].append(i.split(":")[1].split("/")[-1])		
    	for f in FileInfo:
		print f,FileInfo[f]


    elif (sys.argv[1]=="upload"):
	f=doCmd({"cmd":"upload"})
   	url=f
  	#print url
  	datagen, headers = multipart_encode({"sublet": open(sys.argv[2], "rb")})
  	request = urllib2.Request(url, datagen, headers)
	print urllib2.urlopen(request).read() 
   	cache2.getRequest(sys.argv[2])

    elif (sys.argv[1]=="getFile"):
	filename=sys.argv[2]
    	if (not cache2.inCache(filename)):
		(fid,filename)=doCmd({"cmd":"getFile","filename":filename})  
    		print fid
    		url='http://godatacloud.appspot.com/file/'+fid+'/download'
    		print url
		cache2.updateCache(filename,url)
    	response=urllib2.urlopen(url)
    	localFile = open(filename, 'w')
    	localFile.write(response.read())
    	response.close()
    	localFile.close()
    else:
		print "File served from cache folder.Please check"
		


#main()    

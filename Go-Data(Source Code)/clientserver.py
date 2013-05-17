import webapp2
import traceback
import cgi
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from uploadfile import BHandler
from dbtables import FileInfo,Photo
from google.appengine.api import images
from google.appengine.api.users import User
import os
#import client


class MainPage(webapp2.RequestHandler):
    def get(self):
        try:
            self.response.out.write("<html><body>")
            self.main()
        except:
            self.response.out.write("<hr><pre>")
            self.response.out.write(traceback.format_exc())
            self.response.out.write("</pre><hr>")
        finally:
            self.response.out.write("</body></html>")

    def do_view(self):
	filelist=FileInfo.all()
	#print "users.get_current_user()"
	filelist.filter('user =', User('digvijay.singh2808@gmail.com'))

	for file in filelist:
		self.response.out.write("\n<table border=1>\n")
		self.response.out.write("<tr>\n<td>Filename</td><td>%s</td>\n</tr>" % file.blobkey.filename)
		self.response.out.write("<tr>\n<td>Size</td><td>%s</td>\n</tr>" % file.blobkey.size)
		self.response.out.write("<tr>\n<td>User</td><td>%s</td>\n</tr>" % file.user)
		self.response.out.write("<tr>\n<td>Time</td><td>%s</td>\n</tr>" % file.upload_time)
		self.response.out.write("<tr>\n<td>ContentType</td><td>%s</td>\n</tr>" % file.blobkey.content_type)
		self.response.out.write("\n</table>\n")

    def do_upload(self):
	url=blobstore.create_upload_url('http://godatacloud.appspot.com/uploaded')
	
	self.response.out.write("<tr>\n<td>Upload Url</td><td>%s</td>\n</tr>" % url)		    

    def do_getFile(self):
	fid=0
	filename=self.request.get("filename")
	print "Download",filename
	filelist=FileInfo.all()
	print users.get_current_user()
	filelist.filter('user =', User('digvijay.singh2808@gmail.com'))
	for f in filelist:
		if f.blobkey.filename==filename:
			print "YEs",f.blobkey.filename,f.key().id()
			fid=f.key().id()
			break
	#response = urllib2.urlopen("/file/fid/download")
    	#print response
    	print fid
#	response=urllib2.urlopen("godatacloud.appspot.com/file/"+fid+"/download")
#	print fid
#	print response
#	localFile = open(filename, 'w')
#	localFile.write(response.read())
#	response.close()
#	localFile.close()
	self.response.out.write("<tr>\n<td>%s</td><td>%s</td>\n</tr>" % (filename,fid))
	#self.redirect("http://godatacloud.appspot.com/file/"+fid+"/download")
	#print url
	#response=urllib2.urlopen(url)
	#print response.read()
   
    def main(self):
        self.response.out.write("simpleApp3's main here...<br>")
        cmd = self.request.get("cmd", "none")
	print cmd
        methodName = "do_" + cmd
        if (not hasattr(self, methodName)):
            raise Exception("No such cmd: " + cmd)
        else:
            method = getattr(self, methodName)
            method()

app = webapp2.WSGIApplication([
('/client', MainPage),

])

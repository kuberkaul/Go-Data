from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from uploadfile import BHandler
from dbtables import FileInfo,Photo,Apriori
from google.appengine.api import images
from google.appengine.api.users import User
import os
import sys
#import client

class FileUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		blob_info=self.get_uploads()[0]
		typeoffile=blob_info.content_type
		isimage=False
		print typeoffile
		if typeoffile=='image/png' or typeoffile=='image/jpeg':
			isimage=True
			dbentryi=Photo(blobkey=blob_info.key(),serving_url=db.Link(images.get_serving_url(blob_info.key())))
			db.put(dbentryi)
		if (users.get_current_user()):
			dbentry=FileInfo(blobkey=blob_info.key(),user=users.get_current_user(),is_image=isimage)
		else:
			dbentry=FileInfo(blobkey=blob_info.key(),user=User('digvijay.singh2808@gmail.com'),is_image=isimage)
		
		db.put(dbentry)
		accessentry=Apriori(file_id=str(dbentry.key().id()))
		db.put(accessentry)
		self.redirect("/%d" % dbentry.key().id())

app = webapp.WSGIApplication([
('/uploaded', FileUploadHandler),
])
 

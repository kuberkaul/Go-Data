from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from uploadfile import BHandler
from dbtables import FileInfo
import os



class FileUploadHandler(blobstore_handlers.BlobstoreUploadHandler):
	def post(self):
		blob_info=self.get_uploads()[0]
		if self.request.get('folder'):
			folder_name=self.request.get('folder')
		else:
			folder_name="Root"
		if folder_name=="Create New":
			self.redirect("/createfolder/%d" %d dbentry.key().id())
		dbentry=FileInfo(blobkey=blob_info.key(),user=users.get_current_user(),folder=folder_name)
		db.put(dbentry)
		self.redirect("/list/%d" % dbentry.key().id())

app = webapp.WSGIApplication([
('/uploaded', FileUploadHandler),
])
 

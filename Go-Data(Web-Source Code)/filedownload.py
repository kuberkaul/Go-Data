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

class FileDownload(blobstore_handlers.BlobstoreDownloadHandler):
	def get(self,fid):
		file_info=FileInfo.get_by_id(long(fid))
		if not file_info or not file_info.blobkey:
			self.error(404)
			return
		self.send_blob(file_info.blobkey,save_as=True)

app= webapp.WSGIApplication([
('/file/([0-9]+)/download', FileDownload),
])
 

from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from google.appengine.api import images
from uploadfile import BHandler
from dbtables import FileInfo,Photo
import os

class ViewThumbnail(BHandler):
	def get(self,fid):
		imagefile=FileInfo.get_by_id(long(fid))
		image=Photo.all().filter('blobkey =',imagefile.blobkey.key()).get()
		self.render_template("thumbnail.html",{'image':image,'logout_url':users.create_logout_url('/'),
			})
		





app = webapp.WSGIApplication([
('/thumbnail/([0-9]*)', ViewThumbnail),

])

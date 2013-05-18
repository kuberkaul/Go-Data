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

class CreateFolder(BHandler):
	def get(self,fid):
		self.render_template("folder.html",{'fid':fid,'logout_url':users.create_logout_url('/'),})

app = webapp.WSGIApplication([
('/createfolder/([0-9]*)', CreateFolder),

])

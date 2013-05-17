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




class DeleteFile(BHandler):
	def get(self,fid):
		delete_file=FileInfo.get_by_id(long(fid))
		db.delete(delete_file)
		blobstore.delete([delete_file.blobkey])
#		filelist=FileInfo.all()
#		filelist=filelist.filter('user =', users.get_current_user())
		self.redirect("/")
#		self.render_template("list.html",{'filelist':filelist,'logout_url':users.create_logout_url('/'),
#		})

app = webapp.WSGIApplication([
('/delete/(.*)',DeleteFile),

])
 

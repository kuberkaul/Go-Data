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

class ListInfo(BHandler):
	def get(self,fid):
		filelist=FileInfo.all()
		filelist=filelist.filter('user =', users.get_current_user())
		if fid:
			new_file=FileInfo.get_by_id(long(fid))
			if not new_file:
				self.error(404)
				return
			self.render_template("list.html",{'new_file':new_file,'filelist':filelist,'logout_url':users.create_logout_url('/'),
			})
		else:
			self.render_template("list.html",{'filelist':filelist,'logout_url':users.create_logout_url('/'),
			})

		
		
		
app = webapp.WSGIApplication([
('/list/([0-9]*)', ListInfo),

])
 

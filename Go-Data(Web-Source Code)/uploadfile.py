from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from dbtables import FileInfo
import os

class BHandler(webapp.RequestHandler):
	def render_template(self,file,template_args):
		path=os.path.join(os.path.dirname(__file__),"templates",file)
		self.response.out.write(template.render(path,template_args))

class FileUploadForm(BHandler):
	@util.login_required
	def get(self):
		filelist=FileInfo.all()
		if not filelist:
			self.render_template("upload.html",{
				'post_url':blobstore.create_upload_url('/uploaded'),'logout_url':users.create_logout_url('/'),
				})
		else:
			self.render_template("upload.html",{
				'post_url':blobstore.create_upload_url('/uploaded'),'filelist':filelist,'logout_url':users.create_logout_url('/'),
				})
	


app = webapp.WSGIApplication([
('/', FileUploadForm),

])
 
				


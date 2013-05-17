from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util
from dbtables import FileInfo,Apriori
import os
import re
import apriori1
import datetime

MOBILE_PREFIX = '/m/'
MOBI_REG = re.compile(
'(iphone|windows ce|mobile|phone|symbian|mini|pda|ipod|mobi|blackberry|playbook|vodafone|kindle)',
re.IGNORECASE)

class BHandler(webapp.RequestHandler):
	def render_template(self,file,template_args):
		path=os.path.join(os.path.dirname(__file__),"templates",file)
		self.response.out.write(template.render(path,template_args))

class FileUploadForm(BHandler):
	@util.login_required
	def get(self,fid):
		matches=False
		if "iPhone" in self.request.headers["User-Agent"] or "Android" in self.request.headers["User-Agent"]:
			matches=True
		if matches:
			print "Mobile"
			mobile=True
		else:
			print "Desktop"
			mobile=False
		prefetchFilelist=apriori1.fileList

		filelist=FileInfo.all()
		filelist.filter('user =', users.get_current_user())
		
		ua=self.request.headers['User-Agent']
		if fid:
			new_file=FileInfo.get_by_id(long(fid))
			
			if not new_file:
				self.error(404)
				return
			self.render_template("upload.html",{'post_url':blobstore.create_upload_url('/uploaded'),'mobile':mobile,'new_file':new_file,'filelist':filelist,'ua':ua,'logout_url':users.create_logout_url('/'),
			})
		else:
			self.render_template("upload.html",{'post_url':blobstore.create_upload_url('/uploaded'),'mobile':mobile,'filelist':filelist,'ua':ua,'logout_url':users.create_logout_url('/'),
			})


"""
		if not filelist:
			self.render_template("upload.html",{
				'post_url':blobstore.create_upload_url('/uploaded'),'logout_url':users.create_logout_url('/'),
				})
		else:
			self.render_template("upload.html",{
				'post_url':blobstore.create_upload_url('/uploaded'),'filelist':filelist,'logout_url':users.create_logout_url('/'),
				})
	
"""

app = webapp.WSGIApplication([
('/([0-9]*)', FileUploadForm),

])
 
				


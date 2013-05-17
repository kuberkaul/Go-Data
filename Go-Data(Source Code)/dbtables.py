from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

import os

class FileInfo(db.Model):
	blobkey=blobstore.BlobReferenceProperty(required=True)
	user=db.UserProperty(required=True)
	upload_time=db.DateTimeProperty(required=True, auto_now_add=True)
	is_image=db.BooleanProperty()

class Photo(db.Model):
	blobkey=blobstore.BlobReferenceProperty(required=True)
	serving_url=db.LinkProperty()	

class Apriori(db.Model):
	file_id=db.StringProperty()
	timestamp=db.DateTimeProperty(required=True, auto_now_add=True)
	
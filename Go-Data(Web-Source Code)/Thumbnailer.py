import webapp2
from google.appengine.api import images
from google.appengine.ext import blobstore

#To transform an image from the Blobstore in Python, instead of setting the image_data argument of the Image constructor with the image data, set the blob_key argument to the Blobstore key whose value is the image. The rest of the API behaves as expected. The execute_transforms() method returns the result of the transforms, or raises a LargeImageError exception if the result is larger than the maximum size of 32 megabyte.

class Thumbnailer(webapp2.RequestHandler):
    def get(self):
        blob_key = self.request.get("image-blobstore key")
	#set blob_key argument to the blobstore key whose value is the image
        if blob_key:
            blob_info = blobstore.get(blob_key)

            if blob_info:
                img = images.Image(blob_key=blob_key)
                img.resize(width=80, height=100)
                img.im_feeling_lucky()
                thumbnail = img.execute_transforms(output_encoding=images.JPEG)

                self.response.headers['Content-Type'] = 'image/jpeg'
                self.response.out.write(thumbnail)
                return

        # Either "blob_key" wasn't provided, or there was no value with that ID
        # in the Blobstore.
        self.error(404)



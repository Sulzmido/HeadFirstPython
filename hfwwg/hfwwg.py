from django.conf import settings
settings.configure()

#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'django.conf.settings'

import webapp2
#from google.appengine.ext import webapp
#from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
#from google.appengine.ext.db import djangoforms
from django.forms import ModelForm

import hfwwgDB
	
class SightingForm(ModelForm):	
	class _Meta():
		model = hfwwgDB.Sighting

class SightingInputPage(webapp2.RequestHandler):

	def get(self):
		html = template.render('templates/header.html', {'title': 'Report a Possible Sighting'})
		html = html + template.render('templates/form_start.html', {})
		html = html + str(SightingForm())
		html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Sighting'})
		html = html + template.render('templates/footer.html', {'links': ''})
		self.response.out.write(html)

app = webapp2.WSGIApplication([('/.*', SightingInputPage)], debug=True)

		
#app = webapp.WSGIApplication([('/.*', SightingInputPage)], debug=True)

#def main():
	#run_wsgi_app(app)
	
#if __name__ == '__main__':
#	main()
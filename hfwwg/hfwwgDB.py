#from google.appengine.ext import db

#class Sighting(db.Model):
	
	#name = db.StringProperty()
	#email = db.StringProperty()
	#date = db.DateProperty()
	#time = db.TimeProperty()
	#location = db.StringProperty()
	#fin_type = db.StringProperty()
	#whale_type = db.StringProperty()
	#blow_type = db.StringProperty()
	#wave_type = db.StringProperty()
	
from django.db import models

class Sighting(models.Model):
	
	name = models.CharField(max_length = 255)
	
	#class Meta:
	#	abstract = True
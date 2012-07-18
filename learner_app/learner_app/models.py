from mongoengine import *

class Images(Document):
	path = StringField(required=True)
	label = StringField(required=False)
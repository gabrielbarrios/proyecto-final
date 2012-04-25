from django.db import models

class User(models.Model):
	nick_name = models.CharField(max_length = 50)
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)	
	image_profile = models.ImageField(upload_to = 'photo')
	password = models.CharField(max_length = 50)
	birth_date = models.DateField()
	email = models.CharField(max_length = 50)
	location = models.CharField(max_length = 50)
	biography = models.CharField(max_length = 150)

	def __unicode__(self):
		return 'User: %s - %s %s' % (self.pk, self.last_name, self.first_name)

class Tweet(models.Model):
	owner = models.ForeignKey('User')
	status = models.CharField(max_length = 50)
	created_at = models.DateTimeField(auto_now_add=True)

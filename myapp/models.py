from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200, blank=True)
	bio = models.TextField(blank=True, help_text="Short bio or tagline")
	about = models.TextField(blank=True, help_text="Detailed about/background section")
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.name

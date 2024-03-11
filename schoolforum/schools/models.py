from django.db import models


class School(models.Model):
	""" Represents all about the school """

	education_level_choices = [
		('ELEMENTARY', 'Elementary School'),
		('MIDDLE', 'Middle School'),
		('HIGH', 'High School'),
		('COLLEGE', 'College/University'),
		('OTHER', 'Other')
	]

	name = models.CharField("Name", max_length=50)
	description = models.TextField("Description", max_length=500)
	latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=6, null=True, blank=True)
	longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=6, null=True, blank=True)
	country = models.CharField("Country", max_length=100)
	city = models.CharField("City", max_length=100)
	street = models.CharField("Street", max_length=100)
	house_number = models.CharField("House Number", max_length=20, blank=True)
	postal_code = models.CharField("Postal Code", max_length=20, blank=True)
	phone_number = models.CharField("Phone Number", max_length=20, blank=True)
	email = models.EmailField("Email", max_length=254, blank=True)
	website = models.URLField("Website", max_length=200, blank=True)
	education_level = models.CharField("Education Level", max_length=20, choices=education_level_choices, blank=True)
	foundation_date = models.DateField("Foundation Date", null=True, blank=True)

	class Meta:
		db_table = "schools"
		verbose_name = "School"
		verbose_name_plural = "Schools"


class SchoolPhoto(models.Model):
	school = models.ForeignKey(School, related_name='photos', on_delete=models.CASCADE)
	image = models.ImageField("Image", upload_to='school_photos/%Y/%m/%d')

	class Meta:
		db_table = "photos"
		verbose_name = "Photo"
		verbose_name_plural = "Photos"

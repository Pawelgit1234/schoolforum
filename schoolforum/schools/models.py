from django.db import models
from django.utils import timezone


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
		db_table = "school_photos"
		verbose_name = "School Photo"
		verbose_name_plural = "School Photos"


class Discussion(models.Model):
	lesson_type_choices = [
		('MATH', 'Math'),
		('SCIENCE', 'Science'),
		('LANGUAGE', 'Language'),
		('HISTORY', 'History'),
		('ARTS', 'Arts'),
		('MUSIC', 'Music'),
		('PHYSICAL_EDUCATION', 'Physical Education'),
		('COMPUTER_SCIENCE', 'Computer Science'),
		('GEOGRAPHY', 'Geography'),
		('ECONOMICS', 'Economics'),
		('PHILOSOPHY', 'Philosophy'),
		('CHEMISTRY', 'Chemistry'),
		('BIOLOGY', 'Biology'),
		('PHYSICS', 'Physics'),
		('LITERATURE', 'Literature'),
		('RELIGION', 'Religion'),
		('SOCIAL_STUDIES', 'Social Studies'),
		('PSYCHOLOGY', 'Psychology'),
		('CIVICS', 'Civics'),
		('HEALTH', 'Health'),
		('BUSINESS', 'Business'),
		('FOREIGN_LANGUAGE', 'Foreign Language'),
		('FINE_ARTS', 'Fine Arts'),
		('HOME_ECONOMICS', 'Home Economics'),
		('SPORTS', 'Sports'),
		('DRAMA', 'Drama'),
		('JOURNALISM', 'Journalism'),
		('TECHNOLOGY', 'Technology'),
		('AGRICULTURE', 'Agriculture'),
		('ENVIRONMENTAL_SCIENCE', 'Environmental Science'),
		('ENGINEERING', 'Engineering'),
		('CRIMINAL_JUSTICE', 'Criminal Justice'),
		('CAREER_TECHNICAL_EDUCATION', 'Career Technical Education'),
		('PHYSICAL_SCIENCE', 'Physical Science'),
		('ASTRONOMY', 'Astronomy'),
		('ARCHITECTURE', 'Architecture'),
		('NUTRITION', 'Nutrition'),
		('MILITARY_SCIENCE', 'Military Science'),
		('DANCE', 'Dance'),
		('YOGA', 'Yoga'),
		('FILM', 'Film'),
		('ETHICS', 'Ethics'),
		('FORENSICS', 'Forensics'),
		('LINGUISTICS', 'Linguistics'),
		('MEDICINE', 'Medicine'),
		('NURSING', 'Nursing'),
		('PUBLIC_SPEAKING', 'Public Speaking'),
		('WORLD_RELIGIONS', 'World Religions'),
		('STEM', 'STEM'),
		('OTHER', 'Other')
	]

	school = models.ForeignKey(School, related_name='discussions', on_delete=models.CASCADE)
	title = models.CharField("Title", max_length=100)
	content = models.TextField("Content", max_length=500)
	created_at = models.DateTimeField("Created At", default=timezone.now)
	is_closed = models.BooleanField("Is closed", default=False)
	lesson_type = models.CharField("Lesson Type", max_length=20, choices=lesson_type_choices, blank=True)
	rating = models.IntegerField("Rating", default=0)

	class Meta:
		db_table = "discussions"
		verbose_name = "Discussion"
		verbose_name_plural = "Discussions"


class Comment(models.Model):
	user = models.ForeignKey("""Todo: Create User model""", related_name='comments', on_delete=models.CASCADE)
	discussion = models.ForeignKey(Discussion, related_name='discussions', on_delete=models.CASCADE)
	created_at = models.DateTimeField("Created At", default=timezone.now)
	rating = models.IntegerField("Rating", default=0)
	content = models.TextField("Content", max_length=1000)

	class Meta:
		db_table = "comments"
		verbose_name = "Comment"
		verbose_name_plural = "Comments"
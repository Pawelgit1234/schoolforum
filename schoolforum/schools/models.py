import unidecode

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Image(models.Model):
    """ Images for all models """

    image = models.ImageField("Image", upload_to='images/%Y/%m/%d')

    class Meta:
        db_table = "images"
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.image.url


class Rating(models.Model):
    """ Model for rating"""
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    discussion = models.ForeignKey('Discussion', related_name='discussion_ratings', on_delete=models.CASCADE)
    is_plus = models.BooleanField(null=True, blank=True)  # Allow null for no vote

    class Meta:
        db_table = "ratings"
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return f"{self.user.username} - {'Upvote' if self.is_plus else 'Downvote' if self.is_plus is not None else 'No vote'}"


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
    latitude = models.DecimalField("Latitude", max_digits=9, decimal_places=3, null=True, blank=True)
    longitude = models.DecimalField("Longitude", max_digits=9, decimal_places=3, null=True, blank=True)
    country = models.CharField("Country", max_length=100)
    city = models.CharField("City", max_length=100)
    street = models.CharField("Street", max_length=100)
    house_number = models.CharField("House Number", max_length=20, blank=True)
    phone_number = models.CharField("Phone Number", max_length=20, blank=True)
    email = models.EmailField("Email", max_length=254, blank=True)
    website = models.URLField("Website", max_length=200, blank=True)
    education_level = models.CharField("Education Level", max_length=20, choices=education_level_choices, blank=True)
    foundation_date = models.DateField("Foundation Date", null=True, blank=True)
    photos = models.ManyToManyField(Image, related_name='schools_photos', blank=True)
    slug = models.SlugField("Slug", max_length=100, unique=True, blank=True)

    class Meta:
        db_table = "schools"
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode.unidecode(self.name))
        super().save(*args, **kwargs)


class Discussion(models.Model):
    """ From every school """
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

    user = models.ForeignKey(User, related_name='discussion_comments', on_delete=models.CASCADE)
    school = models.ForeignKey(School, related_name='school_discussions', on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=100)
    content = models.TextField("Content", max_length=500)
    created_at = models.DateTimeField("Created At", default=timezone.now)
    is_closed = models.BooleanField("Is closed", default=False)
    lesson_type = models.CharField("Lesson Type", max_length=50, choices=lesson_type_choices, blank=True)
    ratings = models.ManyToManyField(Rating, related_name='discussion_ratings', blank=True)
    photos = models.ManyToManyField(Image, related_name='discussion_photos', blank=True)

    class Meta:
        db_table = "discussions"
        verbose_name = "Discussion"
        verbose_name_plural = "Discussions"

    def overall_rating_balance(self):
        positive_count = self.ratings.filter(is_plus=True).count()
        negative_count = self.ratings.filter(is_plus=False).count()
        return positive_count - negative_count

    def __str__(self):
        return self.title


class Comment(models.Model):
    """ For discussions """
    user = models.ForeignKey(User, related_name='commented_discussions', on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, related_name='discussion_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField("Created At", default=timezone.now)
    content = models.TextField("Content", max_length=1000)
    photos = models.ManyToManyField(Image, related_name='comment_photos', blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    class Meta:
        db_table = "comments"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.content[:10]

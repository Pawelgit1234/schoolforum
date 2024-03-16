from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField("Biography", max_length=500, blank=True)
	date_of_birth = models.DateField("Date of Birth", null=True, blank=True)
	avatar = models.ImageField("Avatar", upload_to='avatars/%Y/%m/%d', blank=True, null=True, default="avatars/default_avatar.jpeg")
	location = models.CharField(max_length=100, blank=True)
	friends = models.ManyToManyField('self', symmetrical=False, blank=True)

	class Meta:
		db_table = "profiles"
		verbose_name = "Profile"
		verbose_name_plural = "Profiles"

	def __str__(self):
		return self.user.username

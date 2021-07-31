from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    photo = models.ImageField(upload_to='user_photos', blank=True)

    def __str__(self):
        return self.user.username


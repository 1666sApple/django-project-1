from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, default='profile_pics.png')
    location = models.CharField(max_length=75, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
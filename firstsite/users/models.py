from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='profile_pic.jpg')
    location = models.CharField(max_length=75, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    website = models.URLField(max_length=200, blank=True)
    birth_date = models.DateField(default=timezone.now, null=True, blank=True)
    birth_place = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    
    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return None
    
    def __str__(self):
        return f'{self.user.username} Profile'

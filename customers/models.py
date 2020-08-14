from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    citizenship = models.CharField(max_length=30)
    country_residence = models.CharField(max_length=30)
    customer_profile_pic = models.ImageField(default="AVATAR.png",null=True,blank=True)



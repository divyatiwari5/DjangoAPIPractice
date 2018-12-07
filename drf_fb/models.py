from django.db import models
from django.utils.text import gettext_lazy as _

# Create your models here.
class FBUserRequest(models.Model):
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    date_joined = models.DateTimeField(verbose_name=_('Date Joined'),)
    first_name = models.CharField(verbose_name=_('First Name'), blank=False, max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), blank=True, null=True, max_length=50)
    phone =  models.CharField(verbose_name=_('Mobile'), max_length=15, unique=True)
    fb_id = models.CharField(verbose_name=_('Facebook ID'), max_length=200, unique=True)
    profile_pic = models.CharField(verbose_name=_('Profile Picture'), max_length=500, blank=True)
    gender = models.CharField(verbose_name=_('Gender'), max_length=10, blank=True)
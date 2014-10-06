from django import forms
from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.hashers import (
    check_password, make_password, is_password_usable)


# Create your models here.

class Detail(models.Model):
	username = models.CharField(max_length=120, unique=True, null=True, blank=True)
	first_Name = models.CharField(max_length=120, null=True, blank=True)
	last_Name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	password = models.CharField(max_length=250)
	confirm_Password = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return smart_unicode(self.email)
	def set_password(self, raw_password):
		self.password = make_password(raw_password)


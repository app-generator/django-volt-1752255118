# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Replace Ont(models.Model):

    #__Replace Ont_FIELDS__
    no = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tt number = models.IntegerField(null=True, blank=True)
    nama teknisi = models.TextField(max_length=255, null=True, blank=True)
    type ont = models.TextField(max_length=255, null=True, blank=True)
    sn before = models.TextField(max_length=255, null=True, blank=True)
    sn after = models.TextField(max_length=255, null=True, blank=True)
    status = models.TextField(max_length=255, null=True, blank=True)
    pic = models.TextField(max_length=255, null=True, blank=True)

    #__Replace Ont_FIELDS__END

    class Meta:
        verbose_name        = _("Replace Ont")
        verbose_name_plural = _("Replace Ont")



#__MODELS__END

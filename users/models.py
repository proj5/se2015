from django.conf import settings
from django.db import models


# Create your models here.


class UserAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile')

    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

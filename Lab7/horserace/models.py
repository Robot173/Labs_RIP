from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Horse(models.Model):
    horse_id = models.AutoField(primary_key=True, unique=True),
    horse_name = models.TextField(max_length=20, blank=True, null=True)
    horse_owner = models.TextField(max_length=80, blank=True, null=True)
    horse_club = models.TextField(max_length=30, blank=True, null=True)
    horse_picture = models.ImageField("Picture", upload_to='img/', blank=True, null=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return "%s" % (self.horse_name)
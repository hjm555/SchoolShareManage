from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=11, null=True, unique=True)
    sex = models.CharField(max_length=1, null=True)
    url = models.CharField(max_length=512, null=True, default='/resources/DefaultUserHeadPicture.png')

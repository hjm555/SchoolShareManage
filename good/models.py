from django.db import models
from user.models import User
import uuid


# Create your models here.
class Good(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, blank=False, db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goodOwnerId')
    type = models.CharField(max_length=10, null=True)
    state = models.CharField(max_length=10, blank=False, null=True, default='未共享')
    description = models.CharField(max_length=200, null=True)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goodBorrowerId', null=True)
    release_time = models.DateTimeField(auto_now_add=True, null=True)


class Picture(models.Model):
    url = models.CharField(max_length=200, blank=False, unique=True)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='pictureGoodId')

    class Meta:
        unique_together = ('url', 'good')


class ShareRequest(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name='requestGoodId')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requestOwnerId')
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requesterId')
    request_time = models.DateTimeField(auto_now_add=True, null=True)
    state = models.CharField(max_length=10, blank=False, default='未处理', null=True)


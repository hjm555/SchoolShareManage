from django.db import models
from user.models import User
import uuid

# Create your models here.


class Message(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messageSenderId')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messageReceiverId')
    content = models.CharField(max_length=200, blank=False)
    send_time = models.DateTimeField(auto_now_add=True, null=True)
    state = models.CharField(max_length=10, default='未读', null=True)

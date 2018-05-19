from django.contrib import admin
from good.models import Good, Picture, ShareRequest

# Register your models here.

admin.site.register([Good, Picture, ShareRequest])

from django.contrib import admin
from .models import DetectedUser, GenderCount

# Register your models here.
admin.site.register(DetectedUser)
admin.site.register(GenderCount)
from django.contrib import admin
from .models import Profile, Group, System

# Register your models here.
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(System)

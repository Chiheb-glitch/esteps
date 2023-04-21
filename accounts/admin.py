from django.contrib import admin
from .models import  Profile , Locations ,Friend,Group,Alert
# Register your models here.

admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Locations)
admin.site.register(Friend)

admin.site.register(Alert)

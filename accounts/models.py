from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.http import JsonResponse


from django.contrib.auth.models import User

from django.db.models.signals import pre_delete, post_save,post_delete


from datetime import datetime

from  channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.dispatch import receiver





class Profile(models.Model):
    step=models.CharField(max_length=10,blank=True,default="0")
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    role = models.CharField(max_length=50,default="")
    bio=models.CharField(max_length=50,default="")
    phone_number = models.CharField(max_length=50,default="test")
    house_location=models.CharField(max_length=150,default="test")
    job_location=models.CharField(max_length=150,default="test")
    studies_location=models.CharField(max_length=150,default="test")
    hobbies_location=models.CharField(max_length=150,default="test")
    is_online = models.BooleanField(default=False)
    def __str__(self):
        return  self.user.username



class Friend(models.Model):
    profile_from = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile3')
    profile_to = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile4')
    status = models.CharField(max_length=10, choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ))


    def __str__(self):
        return f"{self.profile_from} -> {self.profile_to}: {self.status}"




class Locations (models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='location')


    latitude = models.FloatField()
    longitude = models.FloatField()


class Group(models.Model):
    name = models.CharField(max_length=255)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fields = models.TextField(default="")
    visible_to = models.ManyToManyField(Profile, related_name='visible_groups')

    def __str__(self):
        return self.name

class Alert(models.Model):
    alert_sender = models.ForeignKey(Profile, on_delete=models.CASCADE)
    alert_receiver = models.ManyToManyField(Profile, related_name='received_alerts')
    alert_date = models.CharField(max_length=500)
    alert_bio = models.CharField(max_length=500)
    alert_latitude = models.FloatField()
    alert_longitude = models.FloatField()
    checked = models.BooleanField(default=False)


@receiver(post_save,sender=Alert)
def savecart(sender,instance,*args,**kwargs):
        print(instance.alert_sender.user.username)
        channel_layer=get_channel_layer()
        print(channel_layer.group_send)
        print('hani fi post save')
        data={'count':Alert.objects.filter(alert_sender=instance.alert_sender).count(),'current_notification':"item_add"}
        async_to_sync(channel_layer.group_send)( str(instance.alert_sender.user.id),{'type':'send_notification','value':json.dumps(data)})
		


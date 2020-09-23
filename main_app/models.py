from django.db import models
import datetime  
# may need to change 'import datetime' to 'from datetime import datetime'
from django.contrib.auth.models import User
from django.urls import reverse


AVATARS = (
    ('Bard', 'https://i.imgur.com/rPQXpUG.jpg?1'),
    ('Ranger', 'https://i.imgur.com/rPQXpUG.jpg?1'),
)

class System(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    systems = models.ManyToManyField(System)
    date = models.DateTimeField('date of next session', null=True)
    location = models.CharField(max_length=200)
    bio = models.CharField(max_length=2000)
    avatar = models.CharField(
      max_length=255,
      choices=AVATARS,
      # need to change later for either actual images or photos
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile')
    
    def get_systems(self):
        str_all = ''
        for system in self.systems.all():
            str_all += system.name + ', '
        return str_all[:len(str_all) -2]
        

class Group(models.Model):
    group_name = models.CharField(max_length=100)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    date = models.DateTimeField('date of next session')
    location = models.CharField(max_length=100)
    details = models.TextField(max_length=2000)
    players = models.ManyToManyField(Profile, related_name='players')
    contenders = models.ManyToManyField(Profile, related_name='contenders')
    looking = models.BooleanField(default=True)
    
    def __str__(self):
        return self.group_name
    
    def get_absolute_url(self):
        return reverse('groups_index') # TODO: un-stub when we have single group view
    

    
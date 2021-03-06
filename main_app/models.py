from django.db import models
import datetime  
# may need to change 'import datetime' to 'from datetime import datetime'
from django.contrib.auth.models import User
from django.urls import reverse


AVATARS = (
    ('https://i.imgur.com/AHgUoIv.png', 'Rogue'),
    ('https://i.imgur.com/zBHhmmr.png', 'Barbarian (F)'),
    ('https://i.imgur.com/EyeEo9D.png', 'Wizard'),
    ('https://i.imgur.com/tWmY2sU.png', 'Prince'),
    ('https://i.imgur.com/F8k6i3d.png', 'Princess'),
    ('https://i.imgur.com/oE7KZOm.png', 'Bard'),
    ('https://i.imgur.com/x0q6FSr.png', 'Knight'),
    ('https://i.imgur.com/3XXKzWP.png', 'Monk'),
    ('https://i.imgur.com/hyiR7Mi.png', 'Barbarian (M)'),
    ('https://i.imgur.com/9mXtSfN.png', 'Maiden'),
    ('https://i.imgur.com/EO2FsmV.png', 'Queen')
     
)

class System(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    systems = models.ManyToManyField(System, blank=True)
    date = models.DateTimeField('date of next session', null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=2000, blank=True)
    avatar = models.CharField(
      max_length=255,
      choices=AVATARS,
      blank=True
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
    group_name = models.CharField(max_length=100, blank=True)
    system = models.ForeignKey(System, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField('date of next session', blank=True)
    location = models.CharField(max_length=100, blank=True)
    details = models.TextField(max_length=2000, blank=True)
    players = models.ManyToManyField(Profile, related_name='players', blank=True)
    contenders = models.ManyToManyField(Profile, related_name='contenders', blank=True)
    looking = models.BooleanField(default=True, blank=True)
    
    def __str__(self):
        return self.group_name
    
    def get_absolute_url(self):
        return reverse('groups_index') # TODO: un-stub when we have single group view
    

    
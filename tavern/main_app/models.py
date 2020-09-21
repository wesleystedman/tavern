from django.db import models
import datetime  
# may need to change 'import datetime' to 'from datetime import datetime'
from django.contrib.auth.models import User
from django.urls import reverse

SYSTEMS = (
    ('D3.5', 'Dungeons & Dragons 3.5'),
    ('D5', 'Dungeons & Dragons 5'),
    ('P', 'Pathfinder'),
    ('C', 'Call of Cthulu'),
    ('S', 'Starfinder'),
    ('V', 'Vampire: the Masquerade'),
)

AVATARS = (
    ('Bard', 'https://i.imgur.com/rPQXpUG.jpg?1'),
    ('Ranger', 'https://i.imgur.com/rPQXpUG.jpg?1'),
)

class System(models.Model):
    name = models.CharField(max_length=100, choices=SYSTEMS)

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
        return reverse('user_detail', kwargs={'profile_id': self.id})

class Group(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    date = models.DateTimeField('date of next session')
    location = models.CharField(max_length=100)
    details = models.CharField(max_length=2000)
    players = models.ManyToManyField(Profile, related_name='players')
    group_name = models.CharField(max_length=100)
    looking = models.BooleanField()
    contenders = models.ManyToManyField(Profile, related_name='contenders')
    
    def __str__(self):
        return self.group_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'resource_id': self.id})
    

    
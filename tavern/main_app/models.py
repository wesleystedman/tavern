from django.db import models
import datetime  
# may need to change 'import datetime' to 'from datetime import datetime'

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

class Profile(models.Model):
    date = models.DateTimeField('date of next session')
    location = models.CharField(max_length=200)
    bio = models.CharField(max_length=2000)
    avatar = models.CharField(
      max_length=255,
      choices=AVATARS,
      # need to change later for either actual images or photos
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    systems = models.ManyToManyField(System)
  
  
class System(models.Model):
    name = models.CharField(max_length=100)
    
class Group(models.Model):
    group_name = models.CharField(max_length=100)
    system = models.ForeignKey(System)
    date = models.DateTimeField('date of next session')
    location = models.CharField(max_length=100)
    
    

    
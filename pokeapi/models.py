from django.db import models

# Create your models here.
class Pokemon(models.Model):

    name = models.CharField(max_length=30)
    descripction = models.CharField(max_length=255)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

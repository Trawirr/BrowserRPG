from django.db import models
from RanksClasses.models import *
from Regions.models import *
import random

# Create your models here.
class Enemy(models.Model):
    class Meta:
        verbose_name_plural = "enemies"

    rank = models.ForeignKey(CreatureRank, on_delete=models.SET_NULL, null=True, related_name='enemies')
    tier = models.ForeignKey(CreatureClass, on_delete=models.SET_NULL, null=True, related_name='enemies')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='enemies')
    name = models.CharField(max_length=40)

    # battle attributes
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    
    @property
    def all_attributes(self):
        return {'attack': self.attack, 'defense': self.defense, 'agility': self.agility, 'speed': self.speed}
    
    def roll_attack(self):
        return max(1, random.randint(0, self.attributes.attack))
    
    def roll_defense(self):
        return self.attributes.defense
    
    def roll_agility(self):
        return self.attributes.agility
    
    def roll_speed(self):
        return max(1, random.randint(0, self.attributes.speed))
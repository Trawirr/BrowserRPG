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
    
    @property
    def battle_dict(self):
        char_dict = self.all_attributes
        char_dict['name'] = self.name
        char_dict['initiative'] = 0
        char_dict['hp'] = 100

        return char_dict
    
    def roll_attack(self):
        return max(1, random.randint(0, self.attack))
    
    def roll_defense(self):
        return self.defense
    
    def roll_agility(self):
        return self.agility
    
    def roll_speed(self):
        return max(1, random.randint(0, self.speed))
from django.db import models
from RanksClasses.models import *
from Regions.models import *

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
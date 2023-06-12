from django.db import models
from RanksClasses.models import *
from Characters.models import *

class Memory(models.Model):
    class Meta:
        verbose_name_plural = "memories"

    TYPES = models.TextChoices("Type", "WEAPON RANGED_WEAPON ARMOR UTILITY")
    
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, default=None)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)
    memory_type = models.CharField(max_length=13, choices=TYPES.choices, default="WEAPON")
    name = models.CharField(max_length=40)
    description = models.TextField(default="A memory...")
    #is_usable = models.BooleanField(default=False)
    #uses = models.IntegerField(default=0)

    # battle attributes
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    # rest attributes
    heal = models.IntegerField(default=0)

    # expedition attributes
    passage = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)

class Echo:
    pass
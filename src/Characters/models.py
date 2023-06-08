from django.db import models
from django.contrib.auth.models import User
from RanksClasses.models import *
# Create your models here.

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    soul_core = models.IntegerField(default=0)
    shards = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username} {self.rank.name} {self.soul_core} {self.shards}"

# Abstract superclass for Aspect, Ability and Flaw models
class AbilitySuperclass(models.Model):
    class Meta:
        abstract = True

    description = models.TextField(default="Description...")

    # battle attributes
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    agility = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)

    # rest attributes
    heal = models.IntegerField(default=0)
    heal_percent = models.FloatField(default=0.0)

    # expedition attributes
    passage = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    
class Aspect(AbilitySuperclass):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="aspects")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)

    # AKA luck
    prophecy = models.IntegerField(default=0)

class Ability(AbilitySuperclass):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="abilities")

class Flaw(AbilitySuperclass):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="flaws")
from django.db import models
from RanksClasses.models import *

# Create your models here.
class Memory(models.Model):
    # rank = models.IntegerChoices("Rank", "DORMANT AWAKENED ASCENDED TRANSCENDENT SUPREME SACED DIVINE")
    # tier = models.IntegerChoices("Tier", "I II III IV V VI VII")
    rank = models.ForeignKey(Rank)
    tier = models.ForeignKey(Tier)
    type = models.TextChoices("Type", "WEAPON RANGED_WEAPON ARMOR UTILITY")
    description = models.TextField(default="A memory...")
    is_usable = models.BooleanField(default=False)
    uses = models.IntegerField(default=0)

    # battle attributes
    attack = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    dodge = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    initiative = models.IntegerField(default=0)

    # rest attributes
    heal = models.IntegerField(default=0)
    heal_percent = models.FloatField(default=0.0)

    # expedition attributes
    passage = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)

class Echo:
    pass
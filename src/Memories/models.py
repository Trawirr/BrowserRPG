from django.db import models
from RanksClasses.models import *
from Characters.models import *

class Memory(models.Model):
    class Meta:
        verbose_name_plural = "memories"
        ordering = ["-is_equipped", "-rank", "-tier"]

    TYPES = models.TextChoices("Type", "WEAPON ARMOR UTILITY")
    SUBTYPES = models.TextChoices("Type", "MELEE RANGED ARMOR UTILITY SHIELDS")
    
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=True, default=None, related_name="memories")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, related_name="memories")
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True, related_name="memories")
    memory_type = models.CharField(max_length=7, choices=TYPES.choices, default="WEAPON")
    memory_subtype = models.CharField(max_length=7, choices=SUBTYPES.choices, default="MELEE")
    name = models.CharField(max_length=40)
    description = models.TextField(default="A memory...")
    is_equipped = models.BooleanField(default=False)

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

    @property
    def attributes(self):
        return [self.attack, self.defense, self.agility, self.speed, self.heal, self.passage, self.stealth]

    @property
    def attributes_dict(self):
        return {'attack': self.attack, 'defense': self.defense, 'agility': self.agility, 'speed': self.speed, 'heal': self.heal, 'passage': self.passage, 'stealth': self.stealth}
    
    def generate_chatgpt_prompt(self):
        return f"Write a name and a short description (up to 50 words) of {self.memory_subtype} {self.memory_type} artifact from fantasy RPG. This item's attributes are: {self.attributes_dict}"

class Echo:
    pass
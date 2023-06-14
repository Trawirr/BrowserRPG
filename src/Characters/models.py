from django.db import models
from django.contrib.auth.models import User
from RanksClasses.models import *
from Regions.models import *

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="characters")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    soul_core = models.IntegerField(default=0)
    shards = models.IntegerField(default=0)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name="characters")

    def __str__(self) -> str:
        return f"{self.user.username} {self.rank.name} {self.soul_core} {self.shards}"
    
    @property
    def attributes(self):
        attrs = [0 for i in range(8)]
        for a in self.aspects.all():
            aspect_attrs = a.attributes
            attrs = [attrs[i] + aspect_attrs[i] for i in range(len(aspect_attrs))] + [attrs[7]]
            attrs[7] += a.prophecy
            
        for a in self.abilities.all():
            ability_attrs = a.attributes
            attrs = [attrs[i] + ability_attrs[i] for i in range(len(aspect_attrs))] + [attrs[7]]
            
        for a in self.flaws.all():
            flaw_attrs = a.attributes
            attrs = [attrs[i] + flaw_attrs[i] for i in range(len(aspect_attrs))] + [attrs[7]]

        fields = Aspect._meta.get_fields()
        attrs_names = [f.name for f in fields[2:10]]

        attrs_dict = {}
        for k, v in zip(attrs_names, attrs):
            attrs_dict[k] = v

        return attrs_dict


# Abstract superclass for Aspect, Ability and Flaw models
class AbilitySuperclass(models.Model):
    class Meta:
        abstract = True

    name = models.TextField(default="Name...")

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

    def __str__(self) -> str:
        attrs = self.attributes
        if isinstance(self, Aspect): attrs.append(self.prophecy)

        return f"{self.description}, {attrs}"

    @property
    def attributes(self):
        return [self.attack, self.defense, self.agility, self.speed, self.heal, self.passage, self.stealth]
    
class Aspect(AbilitySuperclass):
    # AKA luck
    prophecy = models.IntegerField(default=0)

    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="aspects")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)

class Ability(AbilitySuperclass):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="abilities")

class Flaw(AbilitySuperclass):
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="flaws")
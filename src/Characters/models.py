from django.db import models
from django.contrib.auth.models import User
from RanksClasses.models import *
from Regions.models import *
import random

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="characters")
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True)
    soul_core = models.IntegerField(default=0)
    shards = models.IntegerField(default=0)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name="characters")

    def __str__(self) -> str:
        return f"{self.user.username} {self.rank.name} {self.soul_core} {self.shards}"
    
    @property
    def name(self):
        return self.user.username
    
    @property
    def equipped_memories(self):
        return self.memories.filter(is_equipped=True)
    
    @property
    def all_attributes(self):
        attrs = self.attributes
        attrs_mem = self.memories_attributes

        for k, v in attrs_mem.items():
            attrs[k] += v

        return attrs
    
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
    
    @property
    def memories_attributes(self):
        attrs = [0 for i in range(7)]
        for memory in self.equipped_memories:
            memory_attrs = memory.attributes
            attrs = [attrs[i] + memory_attrs[i] for i in range(len(memory_attrs))]

        fields = Aspect._meta.get_fields()
        attrs_names = [f.name for f in fields[2:9]]

        attrs_dict = {}
        for k, v in zip(attrs_names, attrs):
            attrs_dict[k] = v

        return attrs_dict
    
    def roll_attack(self):
        return max(1, self.attributes.attack + random.randint(0, self.memories_attributes.attack))
    
    def roll_defense(self):
        return self.attributes.defense + random.randint(0, self.memories_attributes.defense)
    
    def roll_agility(self):
        return self.attributes.agility + random.randint(0, self.memories_attributes.agility)
    
    def roll_speed(self):
        return max(1, self.attributes.speed + random.randint(0, self.memories_attributes.speed))

    def roll_stealth(self):
        return max(1, self.attributes.stealth + random.randint(0, self.memories_attributes.stealth))

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
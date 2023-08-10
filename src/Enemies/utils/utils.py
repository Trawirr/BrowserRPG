from Enemies.models import *
import random
import numpy as np
import string

RANKS_TIERS = list(range(1,8))
PROBS = np.array([[1/2**i for i in range(1,8)]]) / sum([1/2**i for i in range(1,8)])

def create_random_sentence(n):
    sentence = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(2,10))) for i in range(n)])
    return sentence[0].upper() + sentence[1:]

def get_model_fields():
    fields = Enemy._meta.get_fields()
    fields = fields[5:]

    return [f.name for f in fields]

def create_enemy_attributes(rank, tier):
    points = 5 + 2**(rank-1) * tier
    attributes = [0 for i in range(4)]

    for i in range(points):
        attributes[random.randint(0, 3)] += 1

    return attributes

def create_enemy_attributes_dict(rank, tier):
    attrs = create_enemy_attributes(rank, tier)
    fields = get_model_fields()
    d = {}
    for i in range(4):
        d[fields[i]] = attrs[i]
    return d

def create_enemy(region: Region) -> Enemy:
    '''Creates a random enemy from the given region'''
    rank, tier = random.choices(RANKS_TIERS, k=2, weights=PROBS.flatten())
    fields_dict = create_enemy_attributes_dict(rank, tier)
    fields_dict['rank'] = CreatureRank.objects.get(value=rank)
    fields_dict['tier'] = CreatureClass.objects.get(value=tier)
    fields_dict['region'] = region
    fields_dict['name'] = create_random_sentence(1)

    return Enemy(**fields_dict)

def get_random_enemy(region: Region) -> Enemy:
    '''Returns a random enemy from the given region'''
    enemies = Enemy.objects.filter(region=region)
    number_of_enemis = enemies.count()
    return enemies[random.randint(0, number_of_enemis-1)]
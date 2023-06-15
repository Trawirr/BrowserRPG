from Memories.models import *
import string
import random
from RanksClasses.models import *
import numpy as np

MEMORY_TYPES = ['WEAPON', 'ARMOR', 'UTILITY']
MEMORY_TYPES_PROBS = [0.3, 0.2, 0.5]
MEMORY_SUBTYPES = {
    'WEAPON': ('MELEE', 'RANGED'),
    'ARMOR': ('ARMOR'),
    'UTILITY': ('', 'SHIELD')
}
MEMORY_SUBTYPES_PROBS = {
    'WEAPON': (0.8, 0.2),
    'ARMOR': (1),
    'UTILITY': (0.9, 0.1)
}
WEAPON_ATTRIBUTES = [0]
ARMOR_ATTRIBUTES = [1]
UTILITY_ATTRIBUTES = []

def create_random_sentence(n):
    sentence = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(2,10))) for i in range(n)])
    return sentence[0].upper() + sentence[1:]

def get_model_fields():
    fields = Memory._meta.get_fields()
    fields = fields[9:]

    return [f.name for f in fields]

def create_memory_attributes(memory_type, rank, tier):
    points = rank + tier
    attributes = [0 for i in range(7)]
    attributes_indices = [i for i in range(7)]
    type_attributes = []
    if memory_type in ["WEAPON"]:
        type_attributes = WEAPON_ATTRIBUTES
    elif memory_type in ["ARMOR"]:
        type_attributes = ARMOR_ATTRIBUTES
    elif memory_type in ["UTILITY"]:
        type_attributes = UTILITY_ATTRIBUTES

    attributes_indices = [i for i in range(7) if i not in type_attributes]

    for index in type_attributes:
        value = random.randint(min(points, rank)//2, min(points, rank))
        attributes[index] = value
        points -= value

    for i in range(tier):
        if points == 0:
            break
        index = attributes_indices.pop(random.randint(0, len(attributes_indices)-1))
        value = random.randint(1, points)
        attributes[index] = value
        points -= value

    return attributes

def create_memory_attributes_dict(memory_type, rank, tier):
    attrs = create_memory_attributes(memory_type, rank, tier)
    fields = get_model_fields()
    d = {}
    for i in range(7):
        d[fields[i]] = attrs[i]
    return d

def create_memory(rank, tier, character):
    memory_type = np.random.choice(MEMORY_TYPES, 1, MEMORY_TYPES_PROBS)[0]
    memory_subtype = np.random.choice(MEMORY_SUBTYPES[memory_type], 1, MEMORY_SUBTYPES_PROBS[memory_type])[0]
    fields_dict = create_memory_attributes_dict(memory_type, rank, tier)
    fields_dict['rank'] = Rank.objects.get(value=rank)
    fields_dict['tier'] = Tier.objects.get(value=tier)
    fields_dict['memory_type'] = memory_type
    fields_dict['memory_subtype'] = memory_subtype
    fields_dict['name'] = create_random_sentence(1)
    fields_dict['description'] = create_random_sentence(10)
    fields_dict['character'] = character

    return Memory(**fields_dict)
from Characters.models import *
import string
import random

def create_random_sentence(n):
    sentence = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(2,10))) for i in range(n)])
    return sentence[0].upper() + sentence[1:]

def create_aspect_attributes(rank):
    points = 7+rank
    max_points = points
    attributes = [0 for i in range(8)]
    attributes_indices = [i for i in range(8)]
    for i in range(8):
        if points <= 0:
            break
        index = attributes_indices.pop(random.randint(0, len(attributes_indices)-1))
        value = min(random.randint(0, points), max_points//2)
        attributes[index] = value
        points -= value
    return attributes

def create_aspect_dict(rank):
    attrs = create_aspect_attributes(rank)
    fields = Aspect._meta.get_fields()
    fields = fields[2:10]
    print(attrs, [f.name for f in fields], sep='\n')
    d = {}
    for i in range(8):
        d[fields[i].name] = attrs[i]
    return d

def create_ability(attributes):
    r = random.randint(1, sum(attributes))
    for i in range(len(attributes)):
        if sum(attributes[:i+1]) >= r: return i, random.randint(2,3)

def create_flaw(rank):
    return random.randint(0,7), -random.randint(1, rank)
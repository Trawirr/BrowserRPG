from Characters.models import *
import string
import random

def create_random_sentence(n):
    sentence = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(2,10))) for i in range(n)])
    return sentence[0].upper() + sentence[1:]

# Generating aspects
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

def get_model_fields(model):
    fields = model._meta.get_fields()
    fields = fields[2:10] if model == Aspect else fields[2:9]

    return [f.name for f in fields]

def create_aspect_attributes_dict(rank, model):
    attrs = create_aspect_attributes(rank)
    fields = model._meta.get_fields()
    fields = fields[2:10] if model == Aspect else fields[2:9]
    print(attrs, [f.name for f in fields], sep='\n')
    d = {}
    for i in range(8):
        d[fields[i].name] = attrs[i]
    return d

def create_aspect(rank, character) -> Aspect:
    fields_dict = create_aspect_attributes_dict(rank, Aspect)
    fields_dict['character'] = character
    fields_dict['name'] = create_random_sentence(1)
    fields_dict['rank'] = Rank.objects.get(value=rank)
    return Aspect(**fields_dict)

def create_ability_attributes(attributes):
    for i, v in enumerate(attributes):
        if v == 0: attributes[i] = 1
    r = random.randint(1, sum(attributes))
    for i in range(len(attributes)):
        if sum(attributes[:i+1]) >= r: return [random.randint(2,3) if j==i else 0 for j in range(len(attributes))]

def create_ability(attributes, character) -> Ability:
    fields = get_model_fields(Ability)
    attributes = create_ability_attributes(attributes)

    fields_dict = {}
    for k, v in zip(fields, attributes):
        fields_dict[k] = v

    fields_dict['character'] = character
    fields_dict['name'] = create_random_sentence(1)

    return Ability(**fields_dict)
    
def create_flaw_attributes(rank):
    attributes = [0 for i in range(7)]
    attributes[random.randint(0,7)] = -random.randint(1, rank)

    return attributes

def create_flaw(rank, character):
    fields = get_model_fields(Flaw)
    attributes = create_flaw_attributes(rank)

    fields_dict = {}
    for k, v in zip(fields, attributes):
        fields_dict[k] = v

    fields_dict['character'] = character
    fields_dict['name'] = create_random_sentence(1)

    return Flaw(**fields_dict)

def battle(char1, char2):
    pass
from Characters.models import *
from Memories.models import *
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

def equip(character: Character, memory: Memory):
    for mem in character.memories.filter(memory_type=memory.memory_type):
        mem.is_equipped = False
        mem.save()

    memory.is_equipped = True
    memory.save()

def check_first(char):
    if isinstance(char, Character):
        if char.equipped_memories.filter(memory_subtype="RANGED"):
            print(char.all_attributes)
            return 1000 + char.all_attributes["speed"]
        return char.all_attributes["speed"]
    else:
        print(char.all_attributes)
        return char.all_attributes["speed"]

def get_first_hit(char):
    attrs = char.all_attributes
    if isinstance(char, Character):
        return round(attrs["attack"] * (1+attrs["stealth"]/10))
    return attrs['attack']

def damage(x):
    return max(0, round(x))

def hit(character1, character2):
    agility1 = character1.roll_agility()
    agility2 = character2.roll_agility()
    if agility1 >= agility2:
        attack, defense = character1.roll_attack(), character2.roll_defense()
        dmg = damage(character1.roll_attack() - character2.roll_defense())
        if dmg == 0:
            return dmg, f"{character1.name} blocked attack"
        else:
            return dmg, f"{character1.name} deals {dmg} damage to {character2.name}."
    else:
        return 0, f"{character2.name} dodges."

def battle(char1, char2):
    character1 = char1.battle_dict
    character2 = char2.battle_dict

    print(character1,"\n", character2, "\n\n")

    battle_logs = []

    # first strike
    if check_first(char1) >= check_first(char2):
        damage_dealt = damage(get_first_hit(char1) - char2.roll_defense())
        character2['hp'] -= damage_dealt
        battle_logs.append(f"{char1.name} deals {damage_dealt} (CRITICAL HIT) damage to {char2.name}.")

    else:
        damage_dealt = damage(get_first_hit(char2) - char1.roll_defense())
        character1['hp'] -= damage_dealt
        battle_logs.append(f"{char2.name} deals {damage_dealt} (CRITICAL HIT) damage to {char1.name}.")

    # main loop
    while character1['hp'] > 0 and character2['hp'] > 0:
        character1['initiative'] += char1.roll_speed()
        character2['initiative'] += char2.roll_speed()

        if character1['initiative'] >= 10 and character2['initiative'] >= 10:
            if character1['initiative'] > character2['initiative']:
                dmg, log = hit(char1, char2)
                character2['hp'] -= dmg
                character1['initiative'] = 0
                battle_logs.append(log)

            else:
                dmg, log = hit(char2, char1)
                character1['hp'] -= dmg
                character2['initiative'] = 0
                battle_logs.append(log)

        if character1['initiative'] >= 10:
            dmg, log = hit(char1, char2)
            character2['hp'] -= dmg
            character1['initiative'] = 0
            battle_logs.append(log)

        if character2['initiative'] >= 10:
            dmg, log = hit(char2, char1)
            character1['hp'] -= dmg
            character2['initiative'] = 0
            battle_logs.append(log)
    
    battle_logs.append(f"{character1['name']} {character1['hp']}hp vs {character2['name']} {character2['hp']}hp")
    if isinstance(char1, Character):
        char1.set_hp(character1['hp'])
        char1.save()
    if isinstance(char2, Character):
        char2.set_hp(character2['hp'])
        char2.save()

    return battle_logs


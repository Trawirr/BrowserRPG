from Regions.models import *
import random
import string

def create_random_sentence(n):
    sentence = ' '.join([''.join(random.choices(string.ascii_lowercase, k=random.randint(2,10))) for i in range(n)])
    return sentence[0].upper() + sentence[1:]

def get_most_isolated_region(regions=None):
    if not regions: regions = Region.objects.all()
    regions = sorted(regions, key=lambda obj: len(obj.adjacent_regions.all()))
    return regions[0]

def create_region():
    name = create_random_sentence(random.randint(1,2))
    adjacent_regions = [get_most_isolated_region()]
    if random.random() < .5:
        adjacent_regions.append(get_most_isolated_region(adjacent_regions[0].adjacent_regions.all()))

    new_region = Region(name=name)
    new_region.save()
    for r in adjacent_regions:
        new_region.adjacent_regions.add(r)

    if new_region.distance_to_gate > 2:
        new_region.gate = True
        new_region.save()
    
    return {'name':name, 'adjacent_regions': adjacent_regions}

if __name__ == "__main__":
    print(get_most_isolated_region())
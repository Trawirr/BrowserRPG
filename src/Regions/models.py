from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=50, default="New region...")
    gate = models.BooleanField(default=False)
    adjacent_regions = models.ManyToManyField('self', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} {'*' if self.gate else ''}"
    
    @property
    def distance_to_gate(self) -> int:
        distance = 0
        visited = []
        to_visit = [self]
        while to_visit:
            to_visit_new = []
            for region in to_visit:
                if region.gate: 
                    return distance
                
                visited.append(region)
                for r in region.adjacent_regions.all():
                    if r not in visited: to_visit_new.append(r)
            to_visit = to_visit_new
            distance += 1

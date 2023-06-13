from django.contrib import admin
from Regions.models import *

# Register your models here.
@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "gate", "count_adjacent", "distance_to_gate")

    def count_adjacent(self, obj):
        return len(obj.adjacent_regions.all())
    
    def distance_to_gate(self, obj):
        return obj.distance_to_gate
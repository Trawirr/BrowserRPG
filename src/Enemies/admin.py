from django.contrib import admin
from Enemies.models import *

@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "rank", "tier", "attack", "defense", "agility", "speed")

    ordering = ("region", "tier", "rank")
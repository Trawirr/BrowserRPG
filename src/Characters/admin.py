from django.contrib import admin
from Characters.models import *

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ("name", "rank", "soul_core", "shards", "attributes")
    ordering = ("rank", "soul_core")

    def name(self, obj):
        return obj.user.username
    
    def attributes(self, obj):
        return obj.attributes

admin.site.register(Aspect)
admin.site.register(Ability)
admin.site.register(Flaw)
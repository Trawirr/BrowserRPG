from django.contrib import admin
from Memories.models import *

# Register your models here.
@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ("name", "memory_type", "rank", "tier")
    ordering = ("rank", "tier")
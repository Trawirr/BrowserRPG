from django.contrib import admin
from Characters.models import *

# Register your models here.
admin.site.register(Character)
admin.site.register(Aspect)
admin.site.register(Ability)
admin.site.register(Flaw)
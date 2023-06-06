from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    # DORMANT = "DO"
    # AWAKENED = "AW"
    # ASCENDED = "AS"
    # TRANSCENDENT = "TR"
    # SUPREME = "SU"
    # SACRED = "SA"
    # DIVINE = "DI"
    # RANK_CHOICES = {
    #     (DORMANT, "Dormant"),
    #     (AWAKENED, "Awakened"),
    #     (ASCENDED, "Ascended"),
    #     (TRANSCENDENT, "Transcendent"),
    #     (SUPREME, "Supreme"),
    #     (SACRED, "Sacred"),
    #     (DIVINE, "Divine"),
    # }
    # rank = models.CharField(max_length=2, choices=RANK_CHOICES, default=DORMANT)
    rank = models.IntegerChoices("Rank", "DORMANT AWAKENED ASCENDED TRANSCENDENT SUPREME SACED DIVINE")
    shards = models.IntegerField(default=0)
    
class Aspect(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

class Ability(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

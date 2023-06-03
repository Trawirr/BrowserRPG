from django.db import models
# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=30)
    DORMANT = "DO"
    AWAKENED = "AW"
    ASCENDED = "AS"
    TRANSCENDENT = "TR"
    SUPREME = "SU"
    SACRED = "SA"
    DIVINE = "DI"
    RANK_CHOICES = {
        (DORMANT, "Dormant"),
        (AWAKENED, "Awakened"),
        (ASCENDED, "Ascended"),
        (TRANSCENDENT, "Transcendent"),
        (SUPREME, "Supreme"),
        (SACRED, "Sacred"),
        (DIVINE, "Divine"),
    }
    rank = models.CharField(max_length=2, choices=RANK_CHOICES, default=DORMANT)
    shards = models.IntegerField(default=0)
    
class Aspect(models.Model):
    pass

class Ability(models.Model):
    pass
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    class Ranks(models.IntegerChoices):
        DORMANT = 1, 'Dormant'
        AWAKENED = 2, 'Awakened'
        ASCENDED = 3, 'Ascended'
        TRANSCENDENT = 4, 'Transcendent'
        SUPREME = 5, 'Supreme'
        SACRED = 6, 'Sacred'
        DIVINE = 7, 'Divine'
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
#    rank_choices = models.IntegerChoices("Rank", "DORMANT AWAKENED ASCENDED TRANSCENDENT SUPREME SACED DIVINE")
    rank = models.IntegerField(choices=Ranks.choices)
    shards = models.IntegerField(default=0)
    
class Aspect(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

class Ability(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

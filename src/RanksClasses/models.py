from django.db import models

# Create your models here.
class Rank(models.Model):
    value = models.IntegerField(default=1, unique=True)
    name = models.CharField(max_length=12, default="Dormant", unique=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.value})"

    def get_next(self):
        if self.value < 7:
            return Rank.objects.get(value=self.value + 1)
        return None
    
class CreatureRank(models.Model):
    value = models.IntegerField(default=1, unique=True)
    name = models.CharField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.value})"

    def get_next(self):
        if self.value < 7:
            return CreatureRank.objects.get(value=self.value + 1)
        return None
    
class CreatureClass(models.Model):
    value = models.IntegerField(default=1, unique=True)
    name = models.CharField(max_length=12, unique=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.value})"

class Tier(models.Model):
    value = models.IntegerField(default=1, unique=True)
    name = models.CharField(max_length=4, unique=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.value})"
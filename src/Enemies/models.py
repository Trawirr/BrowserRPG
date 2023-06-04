from django.db import models

# Create your models here.
class Enemy(models.Model):
    rank = models.IntegerChoices("Rank", "DORMANT AWAKENED FALLEN CORRUPTED GREAT CURSED UNHOLY")
    class_ = models.IntegerChoices("Class", "BEAST MONSTER DEMON DEVIL TYRANT TERROR TITAN")
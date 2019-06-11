import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class QuestPin(models.Model):
    name = models.CharField(max_length=24)
    rank = models.CharField(max_length=1)
    role = models.CharField(max_length=24)
    teamsize = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ]
    )
    duration = models.DurationField()

    def __str__(self):
        return self.name

class QuestDeliverables(models.Model):
    quest_pin = models.ForeignKey(QuestPin, on_delete=models.CASCADE)
    deliverable = models.BooleanField()
    executive_summary = models.BooleanField()
    personas = models.BooleanField()
    ux_map = models.BooleanField()
    information_architecture = models.BooleanField()
    ux_research = models.BooleanField()

    def __str__(self):
        return self.quest_pin.name
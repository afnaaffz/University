from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)])

    def __str__(self):
        return self.course


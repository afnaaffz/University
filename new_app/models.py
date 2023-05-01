from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.course


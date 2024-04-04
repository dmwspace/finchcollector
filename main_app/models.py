from django.db import models

# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField(default=2)

    def __str__(self):
        return self.name
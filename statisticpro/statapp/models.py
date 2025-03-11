from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=255)
    revenue = models.FloatField()
    profit = models.FloatField()
    employees = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

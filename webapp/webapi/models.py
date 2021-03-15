from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name
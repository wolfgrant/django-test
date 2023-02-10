from django.db import models

# Create your models here.

class Demo(models.Model):
    demoNumber = models.IntegerField()

    def __str__(self):
        return f"{self.demoNumber} is a test for my frist database"

class Test(models.Model):
    demoNumber = models.IntegerField()

    def __str__(self):
        return f"{self.demoNumber} is another test number"
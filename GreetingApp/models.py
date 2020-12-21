from django.db import models

class GreetingCard(models.Model):
        name = models.CharField(max_length=100)
        message = models.CharField(max_length=100)

        def __str__(self):
            return self.name

# Create your models here.

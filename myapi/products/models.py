from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)  # String field
    description = models.TextField()  # Long string for descriptions
    price = models.FloatField()  # Float for prices

    def __str__(self):
        return self.name
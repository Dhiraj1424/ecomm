from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=40)
    price=models.FloatField()
    description=models.TextField()
    category=models.CharField(max_length=100)
    discount_price=models.FloatField()
    image=models.CharField(max_length=600)

    def __str__(self):
        return self.name
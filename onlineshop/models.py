from django.db import models

# Create your models here.
class Product(models.Model):
    image_path = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class DescribeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    descipt = models.TextField(max_length=2000)
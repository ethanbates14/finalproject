from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Food(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name

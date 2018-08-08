from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.parent} {self.subcategory_name}"

class Food(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_cat = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name

class Userlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    list_name = models.CharField(max_length=30, blank=False)
    list_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.list_no} {self.list_name} {self.list_date}"

class Listdetail(models.Model):
    ldetail = models.ForeignKey(Userlist, on_delete=models.CASCADE)
    item = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item}"
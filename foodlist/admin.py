from django.contrib import admin

# Register your models here.
from .models import Category, Food, Userlist, Listdetail

admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Userlist)
admin.site.register(Listdetail)
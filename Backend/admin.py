from django.contrib import admin

# Register your models here.
from Backend.models import shop_db, food_db

admin.site.register(shop_db)
admin.site.register(food_db)
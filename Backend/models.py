from django.db import models


class shop_db(models.Model):
    SName = models.CharField(max_length=100, null=True, blank=True)
    OName = models.CharField(max_length=100, null=True, blank=True)
    Place = models.CharField(max_length=100, null=True, blank=True)
    District = models.CharField(max_length=100, null=True, blank=True)
    Contactno = models.IntegerField(null=True, blank=True)


class food_db(models.Model):

    FName = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)

# Create your models here.

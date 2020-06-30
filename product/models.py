from django.db import models
from django.conf import settings

# Create your models here.


USER_MODEL = settings.AUTH_USER_MODEL

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='media/product/images/')
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Purchase(TimeStampModel):
    user = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.IntegerField()


class ItemsBack(TimeStampModel):
    item = models.ForeignKey(Purchase, on_delete=models.SET_NULL, blank=True, null=True)

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from random import randint

# Create your models here.

class Product(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, null=False, blank=False)
    name_product = models.CharField(max_length=30, null=False, blank=False)
    product_description = models.TextField(null=False, blank=False)
    creation_date = models.DateField(default=date.today)
    stock = models.IntegerField(default=1)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name_product

    def save(self, *args, **kwargs):
        if not self.id:
            # if create new tree
            is_id_exist = True
            while is_id_exist:
                id = randint(100000, 1000000)
                is_id_exist = Product.objects.filter(id=id).exists()

            self.id = id

        super().save(*args, **kwargs)
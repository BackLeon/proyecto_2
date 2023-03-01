from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name_contact = models.CharField(max_length=20, null=False, blank=False)
    last_name_contact = models.CharField(max_length=40, null=False, blank=False)
    contact_email = models.EmailField(null=True, blank=False)
    phone = models.CharField(max_length=12, null=False, blank=False)


    def __str__(self):
        return self.first_name_contact




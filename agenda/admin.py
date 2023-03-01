from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_filter = ("last_name_contact", "first_name_contact",)
    list_display = ("first_name_contact", "last_name_contact", "contact_email",)
    search_fields = ("contact_email", "first_name_contact", "last_name_contact")


admin.site.register(Contact, ContactAdmin)

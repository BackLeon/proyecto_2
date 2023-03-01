from django.urls import path
from . import views
from .views import ViewContact, ListContacts, UpdateContact, NewContact, DeleteContact


urlpatterns = [
    path("listcontacts/", ListContacts.as_view(), name="contacts"),
    path("viewcontact/<int:pk>", ViewContact.as_view(), name="viewcon"),
    path("updatecontact/<int:pk>", UpdateContact.as_view(), name="updatecontact"),
    path("deletecontact/<int:pk>", DeleteContact.as_view(), name="deletecontact"),
    path("newcontact/", NewContact.as_view(), name="newcontact"),




]
from django.urls import path
from .views import List, NewProduct, ViewProduct, UpdateProduct, DeleteProduct
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("productlist/", List.as_view(), name="list"),
    path("newproduct/", NewProduct.as_view(), name="newp"),
    path("viewproduct/<int:pk>", ViewProduct.as_view(), name="view"),
    path("updateproduct/<int:pk>", UpdateProduct.as_view(), name="update"),
    path("deleteproduct/<int:pk>", DeleteProduct.as_view(), name="delete"),
]
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
# Create your views here.


class List(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = context["products"].filter(user=self.request.user)
        context["count"] = context["products"].filter(available=True).count()
        busqueda = self.request.GET.get("categoria") or ""
        if busqueda:
            context["products"] = context["products"].filter(category__icontains=busqueda)
        return context

class NewProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "products/new.html"
    context_object_name = "new"
    success_url = reverse_lazy("list")
    fields = ["category", "name_product", "product_description", "stock", "available",]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewProduct, self).form_valid(form)


class ViewProduct(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "products/view.html"
    context_object_name = "product"


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "products/update.html"
    fields = ["category", "name_product", "product_description", "stock", "available", ]
    context_object_name = "product"

    success_url = reverse_lazy("list")


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "products/delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("list")






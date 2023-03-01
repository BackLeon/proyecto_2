from django.shortcuts import render
from .models import Contact
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.


class ListContacts(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "contacts/contactlist.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = context["contacts"].filter(user=self.request.user)
        context["count"] = context["contacts"].filter().count()
        busqueda = self.request.GET.get("first_name") or ""
        if busqueda:
            context["contacts"] = context["contacts"].filter(first_name_contact__icontains=busqueda)
        return context



class ViewContact(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "contacts/viewcontact.html"
    context_object_name = "contact"

class NewContact(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = "contacts/newcontact.html"
    context_object_name = "contact"
    success_url = reverse_lazy("contacts")
    fields = ["first_name_contact", "last_name_contact", "contact_email", "phone",]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NewContact, self).form_valid(form)


class UpdateContact(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = "contacts/updatecontact.html"
    fields = ["first_name_contact", "last_name_contact", "contact_email", "phone",]
    context_object_name = "contact"

    success_url = reverse_lazy("contacts")


class DeleteContact(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = "contacts/deletecontact.html"
    context_object_name = "contact"
    success_url = reverse_lazy("contacts")











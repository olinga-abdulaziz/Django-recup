from django.shortcuts import render
from django.views import generic
from .models import Student
from django.urls import reverse_lazy
# Create your views here.


class HomeView(generic.ListView):
    model=Student
    context_object_name='student'
    template_name = 'app1/home.html'

class DetailView(generic.DeleteView):
    model=Student
    context_object_name='student'
    template_name = 'app1/detail.html'

class AddView(generic.CreateView):
    model=Student
    fields="__all__"
    template_name="app1/add.html"
    success_url=reverse_lazy("home")

class UpdateView(generic.UpdateView):
    model=Student
    context_object_name='student'
    fields="__all__"
    template_name="app1/update.html"

class DeleteView(generic.DeleteView):
    model=Student
    template_name="app1/delete.html"
    success_url=reverse_lazy("home")
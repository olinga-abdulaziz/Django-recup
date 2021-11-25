from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

class RegisterView(generic.CreateView):
    model=User
    template_name="registration/register.html"
    success_url=reverse_lazy('login')

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import authenticate
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.
def myLogin(request):
    context = {"form": authenticate()}
    return render(request, "registration/login.html", context)


def myLogout(request):
    return render(request, "registration/logout.html")


def myProfile(request):
    return redirect(reverse("Products"))


class myRegistration(CreateView):
    model = User
    template_name = "registration/register.html"
    context_object_name = "form"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")

from Account.forms import UserRegistration
from django.shortcuts import render, redirect
from .forms import UserRegistration
# Create your views here.


def registration(request):
    form = UserRegistration()
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')
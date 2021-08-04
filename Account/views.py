from Account.forms import UserRegistration, UserExtendedInfo
from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def registration(request):
    form = UserRegistration()
    ext_form = UserExtendedInfo()
    if request.method == "POST":
        form = UserRegistration(request.POST)
        ext_form  = UserExtendedInfo(request.POST, request.FILES)
        if form.is_valid() and ext_form.is_valid():
            form.save()
            ext_form.save()
            return redirect('login')
    context = {
        'form': form,
        'ext_form': ext_form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

        return redirect('HomePage')


    return render(request, 'login.html')
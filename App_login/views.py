from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            print("Okay")
            login(request, user)
            return HttpResponseRedirect(reverse('App_library:home'))
        else:
            return render(request, 'App_login/login.html', {'error_message': 'Invalid login'})
    return render(request, 'App_login/login.html')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_library:home'))


def forget_password(request):
    return render(request, 'App_login/forget_password.html')

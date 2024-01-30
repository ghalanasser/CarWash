from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Client_Pages:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Client_Pages:home')
            else:
                print(request.user)
                messages.info(request, 'Email or Password is incorrect')

        return render(request, 'Client_Auths/login.html')


def logoutUser(request):
    logout(request)
    return redirect('Client_Auths:login')


def registerPage(request):
    if request.method == 'POST':
        form = User()
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        form.set_password(password)
        form.email = email
        form.username = user_name
        form.save()
        return redirect('Client_Auths:login')
    else:
        form = User()
    return render(request, 'Client_Auths/register.html', {'form': form})

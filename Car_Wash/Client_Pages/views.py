from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import Application_form

def home(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Client_Pages/home.html', {'hide_user_name': hide_user_name, 'user_name': user_name})

def appointment(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Client_Pages/appointment.html', {'hide_user_name': hide_user_name, 'user_name': user_name})

@login_required(login_url='Client_Auths:login')
def apply_appointment(request):
    if request.method == 'POST':
        row = dict()
        row['applicantId'] = request.user.id
        row['userName'] = request.POST.get('userName')
        row['userEmail'] = request.POST.get('userEmail')
        row['carModel'] = request.POST.get('carModel')
        row['plan'] = request.POST.get('plan')
        row['appDate'] = request.POST.get('appDate')
        data = Application_form(row)
        data.save()
    
    return redirect('Client_Pages:home')
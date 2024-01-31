from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import Application_form
from .models import Application_by_user
from django.http import JsonResponse
# from django.urls import reverse


def home(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Client_Pages/home.html', {'hide_user_name': hide_user_name, 'user_name': user_name})

def my_appointments(request):
    user_name = request.user
    hide_user_name = False
    user_id = request.user.id
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
        try:
            apply_app = get_list_or_404(
                Application_by_user, applicantId=user_id)
            print('apply_app',apply_app)
        except Exception as e:
            print(e)
            apply_app = []
        try:
            app_by_user = get_list_or_404(Application_by_user, applicantId=user_id)
            print(app_by_user)
        except Exception as e:
            print(e)
            app_by_user = []
    return render(request, 'Client_Pages/my_appointments.html', {'hide_user_name': hide_user_name, 'user_name': user_name, 'apply_app': apply_app, 'app_by_user': app_by_user})


def delete_object(request, object_id):
    object = get_object_or_404(Application_by_user, id=object_id)
    object.delete()        
    return redirect('Client_Pages:my_appointments')

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
    
    return redirect('Client_Pages:my_appointments')
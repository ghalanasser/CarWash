from django.shortcuts import render
from django.contrib.auth.decorators import login_required

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

# @login_required(login_url='Client_Auths:login')
    # if request.method == 'POST':
    #     row = dict()
    #     row['owner'] = request.user.id
    #     row['petName'] = request.POST.get('petName')
    #     row['petBirthdate'] = request.POST.get('petBirthdate')
    #     row['type'] = request.POST.get('inlineRadioOptions')
    #     row['breed'] = request.POST.get('breed')
    #     row['petImage'] = request.POST.get('petImage')
    #     row['description'] = request.POST.get('description')
    #     data = AdoptionOfferForm(row)
    #     data.save()
    
    # return redirect('Pets:pets')
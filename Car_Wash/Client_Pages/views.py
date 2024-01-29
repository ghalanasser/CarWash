from django.shortcuts import render

def home(request):
    user_name = request.user
    hide_user_name = False
    if user_name and not str(user_name) == 'AnonymousUser':
        hide_user_name = True
    return render(request, 'Client_Pages/home.html', {'hide_user_name': hide_user_name, 'user_name': user_name})
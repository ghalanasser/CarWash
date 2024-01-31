from django.urls import path
from . import views

app_name = 'Client_Pages'
urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('apply_appointment/', views.apply_appointment, name='apply_appointment'),    
    path('my_appointments/', views.my_appointments, name='my_appointments'),    
    path('delete_object/<int:object_id>', views.delete_object, name='delete_object'),    
    path('services/', views.services, name='services'),    
    path('about/', views.about, name='about'),    
    path('contact/', views.contact, name='contact'),    
]
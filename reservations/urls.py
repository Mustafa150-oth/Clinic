from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('reserve/', views.reserve_page, name='reserve'),  
    path('reserve/submit/', views.reserve_appointment, name='submit_reservation'), 
    path('success/', views.success_page, name='success'), 
    
    path('delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('add/', views.add_appointment, name='add_appointment'),
  
    path('receptionist/', views.receptionist_dashboard, name='receptionist_dashboard'),
    path('', views.main_page, name='main_page'),
    path('complaint/', views.complaint_page, name='complaint'),
    path('complaint/submit/', views.submit_complaint, name='submit_complaint'),
    path('complaint/success/', views.complaint_success, name='complaint_success'),
    path('complaint/delete/<int:complaint_id>/', views.delete_complaint, name='delete_complaint'),


    

]

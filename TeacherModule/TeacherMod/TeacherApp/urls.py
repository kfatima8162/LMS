from django.urls import path
from . import views

urlpatterns = [
    path('',views.teacher_dashboard), #http://127.0.0.1:8000/ this will work 
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'), #http://127.0.0.1:8000/dashboard/ = both will open the same page
]
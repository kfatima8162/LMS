from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_view), #http://127.0.0.1:8000/ this will work 
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'), #http://127.0.0.1:8000/dashboard/ = both will open the same page
    path('login/', views.login_view, name = 'login'),
    path('create-assignment/', views.create_assignment, name = 'create_assignment'),
]
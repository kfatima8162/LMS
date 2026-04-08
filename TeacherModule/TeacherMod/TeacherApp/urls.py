from django.urls import path
from .import views 
from .views import dashboard

urlpatterns = [
    path('', dashboard, name = dashboard)
]

from django.shortcuts import render, HtpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')
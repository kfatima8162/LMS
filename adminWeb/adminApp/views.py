from django.shortcuts import render
 
# Admin Dashboard view
def dashboard(request):
    return render(request, 'A_dashboard.html')
 
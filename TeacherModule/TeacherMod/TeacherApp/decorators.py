from django.http import HttpResponse
from django.shortcuts import redirect

def teacher_required(view_func):
    def wrapper(request, *args, **kwargs):
        
        # 🔒 Not logged in
        if not request.user.is_authenticated:
            return redirect('login')

        # ❌ Not a teacher
        if not hasattr(request.user, 'teacher'):
            return HttpResponse("Access Denied: Teachers only 🚫")

        return view_func(request, *args, **kwargs)

    return wrapper

def student_required(view_func):
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')

        if not hasattr(request.user, 'student'):
            return HttpResponse("Access Denied: Students only 🚫")

        return view_func(request, *args, **kwargs)

    return wrapper
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import AssignmentForm
from .decorators import teacher_required

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            
            if hasattr(user, 'teacher'):
                return redirect('teacher_dashboard')
            
            elif hasattr(user, 'student'):
                # return redirect('student_dashboard')
                return HttpResponse("Student module under development 🚧")
            
            else:
                return redirect('login')
                
    return render(request, 'login.html')

@login_required
@teacher_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)

    courses = Course.objects.filter(teacher=teacher)
    total_courses = courses.count()

    students = Student.objects.filter(enrollment__course__in=courses).distinct()
    total_students = students.count()

    assignments = Assignment.objects.filter(course__in=courses)
    total_assignments = assignments.count()

    submissions = Submission.objects.filter(assignment__in=assignments)
    pending_evaluation = submissions.filter(marks__isnull=True).count()

    context = {
        'total_courses': total_courses,
        'total_students': total_students,
        'total_assignments': total_assignments,
        'pending_evaluation': pending_evaluation,
        'courses': courses[:5],
        'assignments': assignments[:5],
    }

    return render(request, 'dashboard.html', context)

@teacher_required
def create_assignment(request):
    teacher = request.user.teacher

    if request.method == "POST":
        form = AssignmentForm(request.POST, request.FILES)

        if form.is_valid():
            assignment = form.save(commit=False)

            # Ensure teacher owns the course
            if assignment.course.teacher != teacher:
                return HttpResponse("Unauthorized", status=401)

            assignment.save()
            return redirect('teacher_dashboard')

    else:
        form = AssignmentForm()

    # ALWAYS set queryset (for both GET & POST invalid)
    form.fields['course'].queryset = teacher.course_set.all()

    return render(request, 'create_assignment.html', {'form': form})
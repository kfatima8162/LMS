from django.shortcuts import render
from .models import *

def teacher_dashboard(request):
    teacher = Teacher.objects.first()

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
from django.contrib import admin
from .models import Department, Course, Subject, Teacher, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display  = ('name',)
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display  = ('code', 'name')
    search_fields = ('name', 'code')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display  = ('code', 'name', 'course')
    search_fields = ('name', 'code')
    list_filter   = ('course',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display   = ('name', 'email', 'department')
    search_fields  = ('name', 'email')
    list_filter    = ('department',)
    filter_horizontal = ('subjects', 'courses')   # nice dual-panel picker


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display  = ('university_roll_no', 'name', 'email', 'branch', 'semester')
    search_fields = ('name', 'email', 'university_roll_no')
    list_filter   = ('branch', 'semester')
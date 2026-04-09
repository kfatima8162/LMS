from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name    = models.CharField(max_length=100)
    code    = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} — {self.name}"


class Subject(models.Model):
    name    = models.CharField(max_length=100)
    code    = models.CharField(max_length=20, unique=True)
    course  = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.code} — {self.name}"


class Teacher(models.Model):
    name       = models.CharField(max_length=150)
    email      = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    subjects   = models.ManyToManyField(Subject, blank=True)
    courses    = models.ManyToManyField(Course,  blank=True)

    def __str__(self):
        return self.name


BRANCH_CHOICES = [
    ('CSE',  'Computer Science & Engineering'),
    ('IT',   'Information Technology'),
    ('ECE',  'Electronics & Communication'),
    ('EE',   'Electrical Engineering'),
    ('ME',   'Mechanical Engineering'),
    ('CE',   'Civil Engineering'),
    ('AI',   'Artificial Intelligence'),
    ('AIML', 'Artificail Intelligence and Machine Learning')
]

SEM_CHOICES = [(i, f'Semester {i}') for i in range(1, 9)]


class Student(models.Model):
    university_roll_no = models.CharField(max_length=30, unique=True,
                                          help_text="University roll number (not class roll no.)")
    name               = models.CharField(max_length=150)
    email              = models.EmailField(unique=True)
    branch             = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    semester           = models.IntegerField(choices=SEM_CHOICES)

    def __str__(self):
        return f"{self.university_roll_no} — {self.name}"
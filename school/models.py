from django.db import models
from django.contrib.auth.models import User

# Class choices
classes = [
    ('one', 'one'), ('two', 'two'), ('three', 'three'),
    ('four', 'four'), ('five', 'five'), ('six', 'six'),
    ('seven', 'seven'), ('eight', 'eight'), ('nine', 'nine'),
    ('ten', 'ten')
]

# Teacher
class TeacherExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

# Student
class StudentExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40, null=True)
    fee = models.PositiveIntegerField(null=True)
    cl = models.CharField(max_length=10, choices=classes, default='one')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

# Attendance
class Attendance(models.Model):
    roll = models.CharField(max_length=10, null=True)
    date = models.DateField()
    cl = models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)

# Notice
class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20, null=True, default='school')
    message = models.CharField(max_length=500)

# Class Schedule
class ClassSchedule(models.Model):
    teacher = models.ForeignKey(TeacherExtra, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    cl = models.CharField(max_length=10, choices=classes)
    date = models.DateField()
    time = models.TimeField()
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject} - {self.cl} - {self.date} {self.time}"



# Assignment
class Assignment(models.Model):
    teacher = models.ForeignKey(TeacherExtra, on_delete=models.CASCADE)
    cl = models.CharField(max_length=10, choices=classes)
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    file = models.FileField(upload_to='assignments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.user.username}"
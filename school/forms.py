from django import forms
from django.contrib.auth.models import User
from .models import  StudentExtra, TeacherExtra, Attendance, Notice,ClassSchedule
from .models import Assignment, AssignmentSubmission


# Admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

# Student forms
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = StudentExtra
        fields = ['roll', 'cl', 'mobile', 'fee', 'status']

# Teacher forms
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']

class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = TeacherExtra
        fields = ['salary', 'mobile', 'status']

# Attendance
presence_choices = (('Present', 'Present'), ('Absent', 'Absent'))
class AttendanceForm(forms.Form):
    present_status = forms.ChoiceField(choices=presence_choices)
    date = forms.DateField()

class AskDateForm(forms.Form):
    date = forms.DateField()

# Notice
class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

# Contact us
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

# Class Schedule
class ClassScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = ClassSchedule
        fields = ['teacher', 'cl', 'subject', 'date', 'time', 'note']


class AssignmentForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Assignment
        fields = ['cl', 'subject', 'title', 'description', 'due_date', 'file']

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ['file']
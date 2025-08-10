from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),

    path('post-assignment/', views.post_assignment_view, name='post-assignment'),
    path('teacher-assignments/', views.teacher_assignment_list, name='teacher-assignment-list'),
    path('teacher-view-submissions/<int:assignment_id>/', views.teacher_view_submissions, name='teacher-view-submissions'),

    path('student-assignments/', views.student_assignment_list, name='student-assignments'),
    path('submit-assignment/<int:assignment_id>/', views.submit_assignment, name='submit-assignment'),

    path('teacher-dashboard/', views.teacher_dashboard_view, name='teacher-dashboard'),
    path('student-dashboard/', views.student_dashboard_view, name='student-dashboard'),

    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
]

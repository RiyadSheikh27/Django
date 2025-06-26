from django.urls import path
from . import views

urlpatterns = [
    path('studentData/', views.studentView, name='students_detail'),
    path('studentInput/', views.studentInput, name='students_Input'),
    path('studentData/<int:pk>/', views.studentDetailView, name='students_Details'),
    # Class Based View
    path('employee/', views.Employees.as_view()),
    path('employeeInput/', views.Employees.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
]
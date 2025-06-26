from django.urls import path
from . import views

urlpatterns = [
    path('studentData/', views.studentView, name='students_detail'),
    path('studentInput/', views.studentInput, name='students_Input'),
    path('studentData/<int:pk>/', views.studentDetailView, name='students_Details'),
]
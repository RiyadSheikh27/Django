from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.studentView, name='students_detail'),
]
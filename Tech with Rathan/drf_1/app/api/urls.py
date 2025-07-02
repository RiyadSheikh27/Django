from django.urls import path, include
from . import views
# for viewset
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('employee', views.EmployeeViewSet, basename='employee')


urlpatterns = [
    path('studentData/', views.studentView, name='students_detail'),
    path('studentInput/', views.studentInput, name='students_Input'),
    path('studentData/<int:pk>/', views.studentDetailView, name='students_Details'),
    # Class Based View
    # path('employee/', views.Employees.as_view()),
    # path('employee/<int:pk>/', views.EmployeeView.as_view()),
    path('',include(router.urls)),

    path('blogs/', views.BlogsView.as_view()),
    path('comments/', views.CommentView.as_view()),

    path('blogs/<int:pk>', views.BlogDetailView.as_view()),
    path('comments/<int:pk>', views.CommentDetailView.as_view()),
]
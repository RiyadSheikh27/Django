from django.urls import path
from . import views


urlpatterns = [
#     Add Task
    path('addTask/', views.addTask, name='addTask'),
#     Mark as Done
    path('mask_as_done/<int:pk>/', views.mask_as_done, name='mask_as_done'),
#     Mark as Undone
    path('mask_as_undone/<int:pk>/', views.mask_as_undone, name='mask_as_undone'),
#     Edit Feature
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
#     Delete Task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),

]

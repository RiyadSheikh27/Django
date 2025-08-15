from django.shortcuts import render
from task.models import Task

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)
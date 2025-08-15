from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def addTask(request):
    """from input-->name="task"""
    task = request.POST.get("task")
    Task.objects.create(title=task)
    return redirect('home')


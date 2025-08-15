from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import get_object_or_404

def addTask(request):
    """from input-->name="task"""
    task = request.POST.get("task")
    Task.objects.create(title=task)
    return redirect('home')


def mask_as_done(request, pk):
    """Mark a task as done"""
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mask_as_undone(request, pk):
    """Mark a task as done"""
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    """Edit a task"""
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        new_title = request.POST.get("task")
        task.title = new_title
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    """Delete a task"""
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')


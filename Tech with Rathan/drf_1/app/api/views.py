from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.
def studentView(request):
    students = Student.objects.all().values()
    students_list = list(students)
    return JsonResponse(students_list, safe=False)
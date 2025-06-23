from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
      students = [
            {
                  "name":"Riyad",
                  "age":25
            },
                        {
                  "name":"Akash",
                  "age":26
            }
      ]
      return HttpResponse(students)
 
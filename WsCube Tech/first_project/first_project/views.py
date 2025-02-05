from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Welcome to my website")

def courseDetails(request,courseId):
    return HttpResponse(courseId)

def homePage(request):
    return render(request,"index.html")
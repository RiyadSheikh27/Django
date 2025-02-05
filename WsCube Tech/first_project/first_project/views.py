from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("Welcome to my website")

def courseDetails(request,courseId):
    return HttpResponse(courseId)

def homePage(request):
    data={
        'title':'Test Home Page',
        'bdata':'Welcome to Homepage',
        'clist':['Java ','C++ ','Python '],
        'std_det_dic':[
            {'name':'Riyad','phn':'016120000'},
            {'name':'Abir','phn':'013070000'}
        ]
    }
    return render(request,"index.html",data)
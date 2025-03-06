from django.http import HttpResponse
from django.shortcuts import render

def userForm(request):
    ans=0
    try:
        n1=int(request.GET['num1'])
        n2=int(request.GET['num2'])
        ans=n1+n2
    except:
        pass
    return render(request,"userform.html",{'output':ans})

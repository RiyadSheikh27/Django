from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
 
def userForm(request):
    ans=0
    data={}
    try:
        if request.method=="POST":
           n1=int(request.POST['num1'])
           n2=int(request.POST['num2'])
           ans=n1+n2
           data={
               'n1':n1,
               'n2':n2,
               'output':ans
           }
    except:
        pass
    return render(request,"userform.html",data)

def submitform(request):
    try:
        if request.method=="POST":
           n1=int(request.POST['num1'])
           n2=int(request.POST['num2'])
           ans=n1+n2
           data={
               'n1':n1,
               'n2':n2,
               'output':ans
           }
           return render(request,"userform.html",data)
    except:
        pass

  

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .form import UserForm
 
def userForm(request):
    ans=0
    fn=UserForm
    data={'form':fn}
    try:
        if request.method=="POST":
           n1=int(request.POST['num1'])
           n2=int(request.POST['num2'])
           ans=n1+n2
           data={
                'form':fn,  
                'output':ans
           }
    except:
        pass
    return render(request,"userform.html",data)

# def submitform(request):
#     pass

  

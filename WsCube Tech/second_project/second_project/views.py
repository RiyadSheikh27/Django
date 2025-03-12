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
def calculator(request):
    c=0
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2 
    except:
        c="Invalid Operation...."

    return render(request,"calculator.html",{'c':c })

  

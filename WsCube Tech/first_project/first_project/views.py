from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to my website")

def courseDetails(request,courseId):
    return HttpResponse(courseId)
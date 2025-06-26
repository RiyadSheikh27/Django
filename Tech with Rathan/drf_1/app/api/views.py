from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
      if request.method == 'GET':
            # Get all the data from the student table
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def studentInput(request):
      if request.method == 'POST':
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                  print(serializer.errors)
                  return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def studentDetailView(request, pk):
      try:
            students = Student.objects.get(pk=pk)
      except Student.DoesNotExist:
            return Response(status=status.HTTP_404_BAD_REQUEST)

      if request.method == 'GET':
            serializer = StudentSerializer(students)
            return Response(serializer.data, status=status.HTTP_200_OK)

      elif request.method == 'POST':
            serializer = StudentSerializer(students, data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                  return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

      elif request.method == "DELETE":
            students.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)






from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class myselfViewset(APIView):
    def post(self, request):
        serializer = serializers.myselfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = get_object_or_404(models.MySelf, id=id)
            serializer = serializers.myselfSerializer(item)
            return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)

        items = models.MySelf.objects.all()
        serializer = serializers.myselfSerializer(items, many=True)
        return Response({"status":"success","data":serializer.data}, status=status.HTTP_200_OK)

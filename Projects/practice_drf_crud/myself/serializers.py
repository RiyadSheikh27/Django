from rest_framework import serializers
from .models import MySelf

class myselfSerializer(serializers.Serializer):
      class Meta:
            model = MySelf
            fields = '__all__'


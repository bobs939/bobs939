# appname/serializers.py
from rest_framework import serializers

class DeviceSerializer(serializers.Serializer):
    # Define serializer fields to match your table columns
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    # Define other fields as needed

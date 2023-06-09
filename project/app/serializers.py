from rest_framework import serializers
from app import models

class UserDataBaseSerializer(serializers.Serializer):
    Firstname=serializers.CharField(max_length=100)
    Lastname=serializers.CharField(max_length=100)
    Email=serializers.EmailField(max_length=100)
    Contact=serializers.IntegerField()

class AdminDataBaseSerializer(serializers.Serializer):
    Firstname=serializers.CharField(max_length=100)
    Lastname=serializers.CharField(max_length=100)
    Email=serializers.EmailField(max_length=100)
    Contact=serializers.IntegerField()
    
class EnquiryDataBaseSerializer(serializers.Serializer):
    Studentname=serializers.CharField(max_length=100)
    Email=serializers.EmailField(max_length=100)
    Contact=serializers.IntegerField()
    Enquiry=serializers.CharField()
    
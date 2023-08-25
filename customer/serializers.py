from rest_framework import serializers
from .models import CustomUser

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','date_of_birth','image' ,'status','student_class']
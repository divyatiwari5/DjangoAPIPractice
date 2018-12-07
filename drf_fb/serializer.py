from rest_framework import serializers
from .models import FBUserRequest

class FBSerializer(serializers.ModelSerializer):
    class Meta:
        model = FBUserRequest
        fields = ('email', 'date_joined', 'first_name', 'phone', 'fb_id', 'profile_pic', 'gender')
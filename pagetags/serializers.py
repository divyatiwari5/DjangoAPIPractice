from rest_framework import serializers
from .models import pagetagModel

class PageTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = pagetagModel
        fields = ("title", "mdesc", "mkeyword", "mschema", "mimage")
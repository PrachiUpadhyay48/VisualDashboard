from rest_framework import serializers
from .models import YourModel


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = YourModel
        fields = '__all__'

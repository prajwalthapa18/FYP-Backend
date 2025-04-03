from rest_framework import serializers
from .models import Person, Count

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'gender']

class CountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Count
        fields = ['male_count', 'female_count']

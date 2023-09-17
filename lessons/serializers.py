from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Lesson

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonOverviewSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Lesson
        fields = ['title', 'instructor', 'image_link']
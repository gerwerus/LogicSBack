from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import *
from django.contrib.auth import get_user_model

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", ]


class UserSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = ["is_staff", "first_name", "last_name", "group", ]

class StudentTestSerializerGet(serializers.ModelSerializer):
    user = UserSerializer()
    passTest = TestSerializer()
    class Meta:
        model = StudentTest
        fields = ['passTime', 'passTest', 'user', 'attempts', 'succses']

class StudentTestSerializerSet(serializers.ModelSerializer):
    class Meta:
        model = StudentTest
        fields = ['passTest', 'user', 'succses']
    def create(self, validated_data):
        instance, created = StudentTest.objects.update_or_create(
            passTest=validated_data['passTest'],
            user=validated_data['user'],         
        )
        if(validated_data['succses'] == True):
            instance.succses = True
        instance.attempts += 1
        instance.save()
        return instance
    def validate(self, attrs):
        data = super().validate(attrs)
        succses = data.get('succses')
        user = data["user"].id
        passTest = data['passTest'].id
        obj = StudentTest.objects.filter(user=user, passTest=passTest, succses=True)
        if(obj):
            raise ValidationError("You passed that set!")
        return data

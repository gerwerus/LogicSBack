from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from .models import *
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from django.contrib.auth import get_user_model
# Create your views here.

class TestAPIList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class TestAPIUpdate(generics.UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminUser, )

class TestAPIDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminUser, )

class UserAPIDetails(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

class GroupAPIList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class StudentTestAPICreate(generics.CreateAPIView):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializerSet
    permission_classes = (IsAuthenticated, )

class StudentTestAPIList(generics.ListAPIView):
    queryset = StudentTest.objects.all()
    serializer_class = StudentTestSerializerGet
    permission_classes = (IsAdminUser, )
    filter_backends = (filters.OrderingFilter, )
    ordering = ('-passTime', )
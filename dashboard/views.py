from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.


class UniversityModelViewSet(viewsets.ModelViewSet):
    queryset = UniversityModel.objects.all()
    serializer_class = UniversitySerializer


class FacultyModelViewSet(viewsets.ModelViewSet):
    queryset = FacultyModel.objects.all()
    serializer_class = FacultySerializer

class GroupModelViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer

class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer

class SubjectModelViewSet(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
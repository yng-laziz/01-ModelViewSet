from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'universities', UniversityModelViewSet)
router.register(r'faculties', FacultyModelViewSet)
router.register(r'groups', GroupModelViewSet)
router.register(r'teachers', TeacherModelViewSet)
router.register(r'subjects', SubjectModelViewSet)
router.register(r'students', StudentModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
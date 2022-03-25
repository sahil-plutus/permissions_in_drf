from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly,\
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly

from rest_framework.response import Response
from .customepermission import MyPermission


# ------------------------- use of django model permissions
# class StudentAPI(ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [DjangoModelPermissions]
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


# ------------------------- use of custom permission
class StudentAPI(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [MyPermission]




# ------------------------- only authenticated user can see list of students
# class StudentView(viewsets.ViewSet):
#
#     def list(self, request):
#         stu = Student.objects.all()
#         serializer = StudentSerializer(stu, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk):
#         if pk is not None:
#             stu = Student.objects.get(id=pk)
#             serializer = StudentSerializer(stu)
#             return Response(serializer.data)
#
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]
    

# ------------------------- only admin user can create and update student information
# class StudentCreateUpdate(viewsets.ViewSet):
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer)
#
#     def update(self, request, pk):
#         if pk is not None:
#             stu = Student.objects.get(id=pk)
#             serializer = StudentSerializer(stu, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]


# ------------------------- only superuser can delete student object
# class StudentDelete(viewsets.ViewSet):
#     def destroy(self, request, pk):
#         stu = Student.objects.get(id=pk)
#         stu.delete()
#         return Response({'msg':'Data Deleted'})
#
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAdminUser]




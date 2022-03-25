
from django.contrib import admin
from django.urls import path, include
from home import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student', views.StudentAPI, basename="student_api")

# router.register('stu', views.StudentView, basename= 'student')
# router.register('stucreate', views.StudentCreateUpdate, basename= 'studentcreate')
# router.register('studel', views.StudentDelete, basename= 'studentdelete')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

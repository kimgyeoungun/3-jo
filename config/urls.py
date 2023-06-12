from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('project/',include('projectapp.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('projectapp.urls')),
    path('project/',include('projectapp.urls')),
    path('admin/', admin.site.urls),
]

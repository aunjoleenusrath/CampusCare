from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('medicine/', include('campusapp.urls')),
    path('mental/', include('mentalsupport.urls')),
    path('health/', include('healthmonitor.urls')),
    path('student/', include('studentsupport.urls')),
]
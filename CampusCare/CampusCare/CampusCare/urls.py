from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('campusapp.urls')),     # your old app
    path('mental/', include('mentalsupport.urls')),  # ✅ new line for your Mental Support app
]

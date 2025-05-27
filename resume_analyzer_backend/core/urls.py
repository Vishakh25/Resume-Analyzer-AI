# resume_analyzer_backend/core/urls.py
from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include your analyzer app's URLs here
    path('api/', include('analyzer.urls')),
]
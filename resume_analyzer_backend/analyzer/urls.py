# resume_analyzer_backend/analyzer/urls.py

from django.urls import path
from .views import AnalyzeResumeView # Make sure to import the specific view class

urlpatterns = [
    path('analyze-resume/', AnalyzeResumeView.as_view(), name='analyze_resume'),
]
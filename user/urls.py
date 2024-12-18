from django.urls import path, include
from .views import RegisterAPIView, AppDownloadViewset
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('app-download/',AppDownloadViewset.as_view({'post':'create', 'get':'list'})),
]

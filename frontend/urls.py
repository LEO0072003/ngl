
from django.urls import path, include
from .views import LandingPageView, LogoutView, AppDetailView, CreateAppView
urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('app-detail/<str:pk>/', AppDetailView.as_view(), name='detail'),
    path('create-app/', CreateAppView.as_view(), name='create-app'),
]

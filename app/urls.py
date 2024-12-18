from os import name
from app.views import (
    AppViewSet,
    CategoryApiView,
    SubCategoryApiView

    )
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('app-crud',AppViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('category/', CategoryApiView.as_view(), name="category"),
  path('sub-category/<int:pk>/', SubCategoryApiView.as_view(), name="category"),
]

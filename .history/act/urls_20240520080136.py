# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RequirementViewSet

router = DefaultRouter()
router.register(r'requirements', RequirementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

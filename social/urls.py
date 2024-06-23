# act/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, PersonViewSet, MediaViewSet, SocialRelationshipViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'medias', MediaViewSet)
router.register(r'socialrelationships', SocialRelationshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

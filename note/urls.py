# note/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NoteRelationViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'relations', NoteRelationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
 
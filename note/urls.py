# note/urls.py

from django.urls import path
from .views import NoteListCreateView, NoteDetailView, NoteRelationListCreateView, NoteRelationDetailView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('relations/', NoteRelationListCreateView.as_view(), name='note-relation-list-create'),
    path('relations/<int:pk>/', NoteRelationDetailView.as_view(), name='note-relation-detail'),
]

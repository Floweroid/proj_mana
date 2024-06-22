# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Todo
from .serializers import  TodoSerializer

# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            # If the input is a list, process each item individually
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            # If the input is not a list, process a single item
            serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


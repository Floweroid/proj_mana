# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,status
from .models import Note, Requirement
from .serializers import NoteSerializer, RequirementSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer


class RequirementCreateAPIView(APIView):
    def post(self, request):
        if isinstance(request.data, list):
            # If the input is a list, process each item individually
            serializer = RequirementSerializer(data=request.data, many=True)
        else:
            # If the input is not a list, process a single item
            serializer = RequirementSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
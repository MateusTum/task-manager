from rest_framework import viewsets
from .models import Task, Group
from .serializers import TaskSerializer, GroupSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from Api.serializers import ProjectSerializer
from Api.models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    

    @action(detail=True, methods=['get'])
    def user_stories(self, request, pk=None):
        project = self.get_object()
        user_stories = project.user_stories.all()
        return Response({'user_stories': [story.title for story in user_stories]})

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

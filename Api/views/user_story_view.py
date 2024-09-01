from rest_framework import viewsets, permissions
from Api.serializers import UserStorySerializer
from Api.models import UserStory

class UserStoryViewSet(viewsets.ModelViewSet):
    serializer_class = UserStorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = UserStory.objects.all()
        project_id = self.kwargs.get('project_id')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

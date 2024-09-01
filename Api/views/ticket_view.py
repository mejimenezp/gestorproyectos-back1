from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from Api.serializers import TicketSerializer
from Api.models import Ticket

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        ticket = self.get_object()
        if ticket.status == 'ACTIVE':
            ticket.status = 'CANCELLED'
            ticket.save()
            return Response({'status': 'Ticket cancelled'})
        else:
            return Response({'status': 'Ticket cannot be cancelled'}, status=400)
    
    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

    def get_queryset(self):
        queryset = Ticket.objects.all()
        user_story_id = self.kwargs.get('user_story_id')
        if user_story_id:
            queryset = queryset.filter(user_story_id=user_story_id)
        return queryset

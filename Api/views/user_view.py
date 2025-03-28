from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from Api.serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

    @action(detail=True, methods=['get'])
    def tickets(self, request, pk=None):
        user = self.get_object()
        tickets = user.tickets.all()
        return Response({'tickets': [ticket.title for ticket in tickets]})

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()



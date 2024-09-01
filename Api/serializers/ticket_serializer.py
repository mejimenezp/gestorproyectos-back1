from rest_framework import serializers
from ..models.ticket import Ticket
from ..models.user_story import UserStory

class UserStorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ['id', 'title']

class TicketSerializer(serializers.ModelSerializer):
    user_story = serializers.PrimaryKeyRelatedField(queryset=UserStory.objects.all())

    class Meta:
        model = Ticket
        fields = ['id', 'title', 'description', 'status', 'user_story', 'assigned_to', 'comments']

    def validate_status(self, value):
        if value not in ['ACTIVE', 'IN_PROGRESS', 'COMPLETED', 'CANCELLED']:
            raise serializers.ValidationError("Invalid status for a ticket.")
        return value

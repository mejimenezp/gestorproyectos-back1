from rest_framework import serializers
from ..models.user_story import UserStory
from ..models.ticket import Ticket

class TicketSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'status']

class UserStorySerializer(serializers.ModelSerializer):
    tickets = TicketSummarySerializer(many=True, read_only=True)
    projectName = serializers.SerializerMethodField()

    class Meta:
        model = UserStory
        fields = ['id', 'title', 'description', 'project', 'projectName', 'tickets']
        read_only_fields = ['tickets', 'projectName']

    def get_projectName(self, obj):
        return obj.project.name if obj.project else 'Unknown'

    def validate_title(self, value):
        if UserStory.objects.filter(title=value).exists():
            raise serializers.ValidationError("A user story with this title already exists.")
        return value

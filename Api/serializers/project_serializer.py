from rest_framework import serializers
from ..models.project import Project
from ..models.user_story import UserStory

class UserStorySummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStory
        fields = ['id', 'title']

class ProjectSerializer(serializers.ModelSerializer):
    user_stories = UserStorySummarySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'company', 'user_stories']
        read_only_fields = ['user_stories']

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError("A project with this name already exists.")
        return value

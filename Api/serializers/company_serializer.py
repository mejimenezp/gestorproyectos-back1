from rest_framework import serializers
from ..models.company import Company
from ..models.project import Project

class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name']

class CompanySerializer(serializers.ModelSerializer):
    projects = ProjectSummarySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'nit', 'phone', 'address', 'email', 'projects']
        read_only_fields = ['projects']

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Please enter a valid email address.")
        return value

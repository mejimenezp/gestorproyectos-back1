from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models.ticket import Ticket

User = get_user_model()

class TicketSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title', 'status']

class UserSerializer(serializers.ModelSerializer):
    tickets = TicketSummarySerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)  

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'company', 'first_name', 'last_name', 'password', 'tickets']
        read_only_fields = ['tickets']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return value

    def create(self, validated_data):
        
        password = validated_data.pop('password')
       
        user = User.objects.create_user(**validated_data, password=password)
        return user

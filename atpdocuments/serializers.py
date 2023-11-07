from rest_framework import serializers
from .models import ATPDocument, ATPDocumentDetails
from django.contrib.auth.models import User

class ATPDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATPDocument
        fields = '__all__'

class ATPDocumentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATPDocumentDetails
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('This username is already in use.')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already in use.')

        return data
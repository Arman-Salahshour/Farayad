from rest_framework import serializers
from Core.models import User

class RegisterUser_serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)
    
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')

        return User.objects.create_user(username=username, email=email, password=password)
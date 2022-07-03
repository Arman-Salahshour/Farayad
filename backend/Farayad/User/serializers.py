from rest_framework import serializers
from Core.models import User

class RegisterUser_serializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'image')
        extra_kawargs={
            'password': {'write_only':True}
        }
    
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        image = validated_data.get('image')
        return User.objects.create_user(username=username, email=email, password=password, image=image)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'image',
        )

class UserFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
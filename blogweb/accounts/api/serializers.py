from accounts.models import User
from rest_framework import serializers

from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},  # Exclude password from response
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        user = super().update(instance, validated_data)
        print(validated_data)
        if password:
            user.set_password(password)
            #print('password:',password)
        
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 50)
    password = serializers.CharField(max_length = 50)

    # def validate(self, data):
    #     username = data.get('username')
    #     password = data.get('password')

    #     if username and password:
    #         user = authenticate(username=username, password=password)
    #         if user:
    #             if user.is_active:
    #                 data['user'] = user
    #             else:
    #                 raise serializers.ValidationError("User account is disabled.")
    #         else:
    #             raise serializers.ValidationError("Incorrect username or password.")
    #     else:
    #         raise serializers.ValidationError("Must include 'username' and 'password'.")
    #     return data

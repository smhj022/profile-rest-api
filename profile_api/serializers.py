from rest_framework import serializers

from .models import UserProfile

# serializer is a feature from django from a rest framework that allows you to/
# easily convert data inputs into python objects and vice versa.


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing over view """

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # override the create function with the create user function /
    # if we use create function then the password will be saved in character /
    # but we want to save the password as hash so we need to use create_user function /
    # that we have created in the model

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"]
        )

        return user

    # override the update because if password is updated the it should be saved as hash
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

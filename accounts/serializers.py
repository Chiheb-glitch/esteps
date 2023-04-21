from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture']  # Specify the fields you want to include in the profile creation

    def create(self, validated_data):
        user = self.context['request'].user  # Get the user from the token
        profile_picture = validated_data.get('profile_picture')  # Get the profile picture from the request data

        # Create the profile instance
        profile = Profile(
            user=user,
            profile_picture=profile_picture,
            role='default_role',  # Set the default role here
            is_online=False  # Set the default online status here
        )
        profile.save()
        return profile

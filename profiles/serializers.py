from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    image = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'image', 'created_at']

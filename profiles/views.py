from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    
class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile.
    Only the owner of the profile can update it.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class ProfileList(generics.ListCreateAPIView):
    """
    List all profiles.
    Only authenticated users can view the list of profiles.
    Profile creation is handled by Django signals, so no need for a create view here.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
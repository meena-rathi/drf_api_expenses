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

class ImageUploadView(APIView):
    def post(self, request, format=None):
        if 'image' not in request.FILES:
            return Response({'error': 'No image uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        image = request.FILES['image']
        # Find the profile to which the image should be attached
        # You may need to determine how to associate the image with a profile.
        # Example: assuming the user is uploading an image for their own profile.
        profile = Profile.objects.get(owner=request.user)
        profile.image = image
        profile.save()

        serializer = ProfileSerializer(profile)
        return Response({'message': 'Image uploaded successfully', 'profile': serializer.data}, status=status.HTTP_200_OK)

from django.urls import path
from .views import ProfileDetail, ProfileList, ImageUploadView  # Import classes from views.py

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('profiles/', ImageUploadView.as_view(), name='upload_image'),
]
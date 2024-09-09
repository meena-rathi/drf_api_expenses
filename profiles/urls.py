from django.urls import path
from .views import ProfileDetail, ProfileList

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),  # This matches /profiles/
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),  # This matches /profiles/<int:pk>/
]
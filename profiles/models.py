from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='../default_profile_qdjgyp')

    def __str__(self):
        return f"{self.owner}'s profile"

# Signal to create or update the Profile when a User is created or saved

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

def save_profile(sender, instance, **kwargs):
    instance.profile.save()
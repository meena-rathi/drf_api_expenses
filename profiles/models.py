from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp'
    )
    created_at = models.DateTimeField(default=timezone.now) # Add this line


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)

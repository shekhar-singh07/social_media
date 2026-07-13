from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    
    img=models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    owner=models.OneToOneField(User ,on_delete=models.CASCADE)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.owner.username
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.

class CustomerUser(AbstractUser):
    name = models.CharField(null = True, blank=True, max_length=100)
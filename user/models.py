from django.db import models
from app.models import App
from django.contrib.auth.models import User

# Create your models here.

class UserAppDownload(models.Model):
    """Model to store the """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='app_ss/')

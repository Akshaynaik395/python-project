from django.db import models

# Create your models here.
class home(models.Model):
    image=models.ImageField(upload_to='images/')

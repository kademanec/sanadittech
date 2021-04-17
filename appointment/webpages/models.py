from django.db import models
from datetime import datetime
# Create your models here.

class BookApp(models.Model):
    username=models.CharField(max_length=256),
    first_name=models.CharField(max_length=256),
    dateApp=models.DateTimeField(blank=True),

    def __str__(self):
        return self.first_name



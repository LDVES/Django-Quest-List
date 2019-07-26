from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Quest(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=50)
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quests_manager:index')

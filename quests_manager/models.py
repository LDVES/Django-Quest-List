from django.db import models

# Create your models here.
class Quest(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
#Return Quest title as the name of object
    def __str__(self):
        return self.title

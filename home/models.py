from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    page_name_choices = [
    ('Homepage','homepage'),
    ('About_us', 'about_us'),
    ('Contact', 'contact'),
    ]
    page_name = models.CharField(max_length=100, choices = page_name_choices, default='Homepage', unique=True)

    def __str__(self):
        return self.title

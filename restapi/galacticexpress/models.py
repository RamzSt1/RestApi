from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=256, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

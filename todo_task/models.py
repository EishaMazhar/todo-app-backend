from django.db import models


# Create your models here.
class TodoTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # priority = models.Choices([("High", "High"), ("Low", "Low"), ("Medium", "Medium"), ("Not_specified", "Not specified")])


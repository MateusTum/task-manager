from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name

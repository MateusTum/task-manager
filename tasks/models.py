from django.db import models

# Create your models here.

class Group(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('N', 'Normal'),
        ('H', 'High'),
        ('VH', 'Very High'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='N')

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('N', 'Normal'),
        ('H', 'High'),
        ('VH', 'Very High'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    priority = models.CharField(max_length=2, choices=PRIORITY_CHOICES, default='N')

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name

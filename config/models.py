from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Application(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    url = models.URLField(max_length=200, verbose_name='URL')
    
    def __str__(self) -> str:
        return self.name
    
class Task(models.Model):
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    task_description = models.CharField(max_length=255, null=True)
    application = models.ForeignKey(Application, related_name='tasks', on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Pipeline', 'Pipeline'),
        ('In Progress', 'In Progress'),
        ('On Hold', 'On Hold'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Pipeline')
    deadline = models.DateField()

    def __str__(self):
        return self.task_description

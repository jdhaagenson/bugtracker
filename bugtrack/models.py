from django.db import models
from customuser.models import CustomUser
from django.utils import timezone



class Ticket(models.Model):
    STATUS_OPTIONS = [
        'New', 'In Progress', 'Invalid', 'Done'
    ]
    title = models.CharField(max_length=150)
    time_created = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=STATUS_OPTIONS, default='New')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)
    completed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True)

from django.db import models
from customuser.models import CustomUser
from django.utils import timezone


class Ticket(models.Model):
    NEW = 'New'
    ASSIGNED = 'In Progress'
    INVALID = 'Invalid'
    COMPLETE = 'Done'
    STATUS_CHOICES = [
        (NEW, 'New'),
        (ASSIGNED, 'In Progress'),
        (INVALID, 'Invalid'),
        (COMPLETE, 'Done')
    ]
    title = models.CharField(max_length=150)
    time_created = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=250)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_by')
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default=NEW)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True, blank="True", related_name='assigned_to')
    completed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None, null=True, blank='True', related_name='completed_by')

    def __str__(self):
        return self.title

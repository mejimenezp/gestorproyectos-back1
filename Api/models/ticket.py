from django.db import models
from .user_story import UserStory
from .user import User

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE, related_name='tickets', verbose_name="User Story")
    title = models.CharField(max_length=255, verbose_name="Ticket Title")
    description = models.TextField(verbose_name="Ticket Description")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ACTIVE', verbose_name="Status")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets', verbose_name="Assigned To")
    comments = models.TextField(blank=True, null=True, verbose_name="Comments")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.title} - {self.user_story.title} ({self.status})"
    
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

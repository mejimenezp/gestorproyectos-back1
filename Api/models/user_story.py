from django.db import models
from .project import Project

class UserStory(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='user_stories', verbose_name="Project")
    title = models.CharField(max_length=255, verbose_name="User Story Title")
    description = models.TextField(verbose_name="User Story Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.title} - {self.project.name}"
    
    class Meta:
        unique_together = ('project', 'title')
        verbose_name = "User Story"
        verbose_name_plural = "User Stories"

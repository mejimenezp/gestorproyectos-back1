from django.db import models
from .company import Company

class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects', verbose_name="Company")
    name = models.CharField(max_length=255, verbose_name="Project Name")
    description = models.TextField(blank=True, null=True, verbose_name="Project Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.name} - {self.company.name}"
    
    class Meta:
        unique_together = ('company', 'name')
        verbose_name = "Project"
        verbose_name_plural = "Projects"

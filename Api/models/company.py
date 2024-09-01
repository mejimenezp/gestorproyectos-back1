from django.db import models
from django.core.validators import RegexValidator, EmailValidator

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Company Name")
    nit = models.CharField(max_length=20, unique=True, validators=[RegexValidator(r'^\d{6,20}$')], verbose_name="NIT")
    phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?\d{7,15}$')], verbose_name="Phone")
    address = models.CharField(max_length=255, verbose_name="Address")
    email = models.EmailField(validators=[EmailValidator()], verbose_name="Email")

    def __str__(self):
        return f"{self.name} (NIT: {self.nit})"
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

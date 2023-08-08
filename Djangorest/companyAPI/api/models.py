from django.db import models

# Create your models here.


# company model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    company_location = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50, choices=(
        ('IT', 'IT'), ('NON IT', 'NON IT'), ('None', 'None'),))
    company_about = models.CharField(max_length=50)
    company_crated = models.DateTimeField(auto_now=True)
    company_active = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


# employee mode
class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_email = models.CharField(max_length=50)
    employee_address = models.CharField(max_length=50)
    employee_phone = models.CharField(max_length=50)
    employee_about = models.CharField(max_length=50)
    employee_position = models.CharField(max_length=50, choices=(
        ('manager', 'manager'), ('software developer', 'software developer'), ('project manager', 'project manager'),))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

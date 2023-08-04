from django.db import models

# Create your models here.

# company model


class company(models.Model):
    company_i = models.AutoField(primary_key=True)
    name_company = models.CharField(max_length=50)
    locations = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100, choices=(('IT', 'IT'), ('Non IT', 'Non IT'), ('Mobiles phone', 'Mobiles phone')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_company

# employee model


class employee(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField
    position = models.CharField(max_length=100, choices=(
        ("Manager", "Manager"), ("software developer", "sd"), ("project Manager", "project Manager")))

    Company = models.ForeignKey(company, on_delete=models.CASCADE)

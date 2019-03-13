from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Employee(models.Model):

    name = models.CharField(max_length = 42)

    age = models.IntegerField(
            null = False,
            blank = False,
            validators = [MaxValueValidator(100), MinValueValidator(18)] 
        )

    salary = models.IntegerField(
            null = False,
            blank = False,
            validators = [MaxValueValidator(10**8), MinValueValidator(10000)] 
        )

    created_date = models.DateTimeField(auto_now_add = True, null = False, blank = False) 
    modified_date = models.DateTimeField(auto_now = True, null = False, blank = False)

    reporting_manager = models.ForeignKey(
            to = 'self', 
            on_delete = models.SET_NULL, 
            null = True, 
            blank = True
        )

    DES_CHOICES = (
        ('J', 'Janitor'),
        ('C', 'Chef'),
        ('S', 'Secretary'),
        ('CEO', 'Chief Executive Officer'),
        ('VP', 'Vice President'),
        ('D', 'Developer'),
        ('PM', 'Project Manager'),
        ('JD', 'Junior Developer'),
        ('HR', 'Human Resources Representative'),
        ('M', 'Marketer'),
        ('S', 'Salesperson'),
        ('QAE', 'Quality Assurance Engineer')
    )

    designation = models.CharField(max_length = 3, choices = DES_CHOICES)

    def __str__(self):
        return self.name
    
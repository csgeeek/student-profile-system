from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class InstitutionHead(AbstractUser):
#     institution_id = models.CharField(max_length=4, unique=True)
#     institution_name = models.CharField(max_length=150, unique=True)
#     can_edit = models.BooleanField(default=True)
#     USERNAME_FIELD = 'institution_id'

# class Go


class Student(models.Model):
    # institution_id = models.ForeignKey(
    #     InstitutionHead, on_delete=models.CASCADE)
    institution_id = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    other_details = models.CharField(max_length=100)

    def __str__(self):
        return self.name

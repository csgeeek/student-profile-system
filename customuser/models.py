from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, first_name=None, last_name=None):
        user = self.model(username=username, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, first_name=None, last_name=None):
        user = self.create_user(username, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_college_head = models.BooleanField(default=False)
    is_govt_official = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username


class College(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['college_id',]),
        ]
    college_id = models.CharField(max_length=4, unique=True)
    college_name = models.CharField(max_length=255, unique=True)
    college_head = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="college_head")

    def __str__(self):
        return self.college_id


class Student(models.Model):
    class Meta:
        unique_together = (("college_id", "registration_no"),)
        indexes = [
            models.Index(fields=['college_id',])
        ]
    college_id = models.ForeignKey(College, on_delete=models.CASCADE, related_name="student_college_id")
    registration_no = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    other_details = models.CharField(max_length=200)
    student_college_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.college_id) + str(self.registration_no)

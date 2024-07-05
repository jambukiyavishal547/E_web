from django.db import models

# Create your models here.
class Student(models.Model):
    class Gender(models.TextChoices):
         MALE = 'M', 'MALE'
         FEMALE = 'F', 'FEMALE'
         OTHERS = 'O', 'OTHERS'

    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=Gender.choices)
    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
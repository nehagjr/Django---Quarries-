from django.db import models

# Create your models here.

class Student(models.Model):
    Student_nm=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    dep_nm=models.CharField(max_length=20)

    def __str__(self):
        return self.Student_nm    
    
    class Meta:
        db_table='Student'
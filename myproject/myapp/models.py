from django.db import models

# Create your models here.
class Department(models.Model):
    department=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering=['department']

class StudentId(models.Model):
    student_id=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class student(models.Model):
    department=models.ForeignKey(Department,related_name='depart' ,on_delete=models.CASCADE)
    student_id=models.OneToOneField(StudentId, related_name="stude", on_delete=models.CASCADE)
    studentname=models.CharField(max_length=100)
    studentemail=models.EmailField(unique=True)
    studentage=models.CharField(max_length=10)
    student_address=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.studentname
    
    class Meta:
        ordering=['studentname']
        verbose_name="student"
from faker import Faker
fake= Faker()
import random
from .models import *

def whatever(n=10)->None:
    try:
        for _ in range(0,n):
            depart_qry= Department.objects.all()
            depart_random_index=random.randint(0,len(depart_qry)-1)
            department_id=depart_qry[depart_random_index]
            studeStudentId=f'STU-0{random.randint(100,500)}'
            studentname=fake.name()
            studentemail=fake.email()
            studentage=random.randint(20,30)
            student_address=fake.address()

            student_id_obj=StudentId.objects.create(student_id=studeStudentId)

            student_create=student.objects.create (
                department=department_id,
                student_id=student_id_obj,
                studentname=studentname,
                studentemail=studentemail,
                studentage=studentage,
                student_address=student_address
                )
    except Exception as e:
        print(e)

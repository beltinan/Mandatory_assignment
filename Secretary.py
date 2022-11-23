from Course import Course
from Student import Student

course1=Course("D1", "Danish101","Beginner")
course2=Course("D2", "Danish102","Intermediate")
course3=Course("D3", "Danish103","Advanced")

student1=Student("Firat", "22", "firat@gmail.com")
student2=Student("Bunyamin", "20", "bunyamin@gmail.com")
student3=Student("Emir", "19", "emir@gmail.com")

student4=Student("Sigurd", "20", "sigurd@gmail.com")
student5=Student("Has", "23", "has@gmail.com")
student6=Student("Jones", "21", "jones@gmail.com")

student7=Student("Klaus", "21", "klaus@gmail.com")
student8=Student("Sam", "22", "sam@gmail.com")
student9=Student("Lars", "22", "lars@gmail.com")


course1.add_student(student1)
course1.add_student(student2)
course1.add_student(student3)

course2.add_student(student4)
course2.add_student(student5)
course2.add_student(student6)

course3.add_student(student7)
course3.add_student(student8)
course3.add_student(student9)

print("------------------ User story 4 -------------------")
c_name= input("What is the name of the course? ")
if(c_name=="Danish101"):
    returned_list=course1.get_list(course1)
    for stu in returned_list:
        print(f"Name: {stu.student_name}, Age: {stu.student_age}, Email: {stu.student_email}")

elif(c_name=="Danish102"):
    returned_list = course2.get_list(course2)
    for stu in returned_list:
        print(f"Name: {stu.student_name}, Age: {stu.student_age}, Email: {stu.student_email}")

elif(c_name=="Danish103"):
    returned_list = course2.get_list(course2)
    for stu in returned_list:
        print(f"Name: {stu.student_name}, Age: {stu.student_age}, Email: {stu.student_email}")

else:
    print("Wrong course name")

print("------------------ User story 5 -------------------")
cname=input("What is your course? ")
semail=input("What is your email ")
if(cname=="Danish101"):
    found_student= course1.get_by_email(course1, semail)
    print(f"Result: {found_student.student_name}")
elif(cname=="Danish102"):
    found_student= course2.get_by_email(course2, semail)
    print(f"Result: {found_student.student_name}")
elif(cname=="Danish103"):
    found_student= course3.get_by_email(course3, semail)
    print(f"Result: {found_student.student_name}")
else:
    print("Error")

print("------------------ User story 6 -------------------")
coursename=input("What is your course? ")
studentemail=input("What is your email ")
if(coursename=="Danish101"):
    student_to_remove=course1.get_by_email(course1,studentemail)
    course1.remove_student(student_to_remove)
    for stu in course1.student_list:
        print(f"Updated Name list: {stu.student_name}, Updated Email List: {stu.student_email}")
elif(coursename=="Danish102"):
    student_to_remove=course2.get_by_email(course2,studentemail)
    course2.remove_student(student_to_remove)
    for stu in course2.student_list:
        print(f"Updated Name list: {stu.student_name}, Updated Email List: {stu.student_email}")
elif(coursename=="Danish103"):
    student_to_remove=course3.get_by_email(course3,studentemail)
    course3.remove_student(student_to_remove)
    for stu in course3.student_list:
        print(f"Updated Name list: {stu.student_name}, Updated Email List: {stu.student_email}")
else:
    print("Error")

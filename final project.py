import random
from course import Course
from classes import Student

courses_list=[]
student_list=[]
student_courses=[]
def find_Course (course_name,courses):
    index=0
    for i in courses:
        if i.course_name in course_name:
            return index
        return -1
def find_student(student_number, student_list):
    index=0
    for i in student_list:
        if i.student_number in student_number:
            return index
        return -1

def add ():
    number = str(input('Enter student number : '))
    if student_number == number:
        course = input('Enter Course Name : ')
    if course_name == course:
        student_courses.append(course)
        student_list.extend(student_courses)
    print('the course will add .......')
def display ():
    print('the details of student ..............\n')
    for i in student_list:
        print('the name is :',i.student_name,
              '\nthe class of student is :',i.student_class,
              '\nthe course of student is :',student_courses.append(course))
while True:
    print('Select choice please ....')
    print("---------------------------------------------------------")
    x=int(input(" 1.Add New Student \t\t\t 2.Remove student \n 3.Edit Student \t\t\t 4.Display All Students \n 5.Create New Course \t\t 6.Add Course To The Student \n 0.Exit \n"))
    if x==1 :
        student_number = str(random.randint(1, 10))
        student_name = input("Enter student name : ")
        while True:
            student_class = input("Enter student class (A\B\C) : ")
            if student_class in ["A", "B", "C"]:
                break

        student = Student(student_number, student_name, student_class)
        student_list.append(student)
        print("---------------------------------------------------------")
        print("student number \t\t student name \t\t student Class")
        print("---------------------------------------------------------")
        for i in student_list:
            print(i.student_number, "\t\t\t\t\t", i.student_name, "\t\t\t\t\t", i.student_class)
        print("student saved successfully")
    elif x==2 :
         id=str(input('Enter the id number : '))
         if id==student_number:
            student_list.remove(student)
            print('delete done successful')
         else:
             print('the user doesnt exit')
    elif x==3 :
        id = str(input('Enter the id number : '))
        if id==student_number:
            student.setname(input('Enter new name : '))
            student.setclass(input('Enter Student Class [A/B/C] :'))
            student_name=student.getname()
            student_class=student.getclass()
            student = Student(student_number, student_name, student_class)
            print('After Edit : ')
            print("---------------------------------------------------------")
            print("student number \t\t student name \t\t student Class")
            print("---------------------------------------------------------")
            for i in student_list:
                print(i.student_number, "\t\t\t\t\t", i.student_name, "\t\t\t\t", i.student_class)

        else:
            print('user Not defined')
    elif x==4 :
        print("---------------------------------------------------------")
        display()
    elif x == 5:
        course_name = input("Enter course name : ")
        course_class = None
        while True:
            course_class = input("Enter course class (A\B\C) : ")
            if course_class in ["A", "B", "C"]:
                break

        course = Course(course_name, course_class)
        courses_list.append(course)
        print("course created successfuly ")

    elif x==6 :
       add()

    elif x==0:
        exit()
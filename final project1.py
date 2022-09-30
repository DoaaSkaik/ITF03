import random
from course import Course
from student import Student

courses_list=[]
student_list=[]
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
while True:
    print("---------------------------------------------------------")
    x=int(input(" 1.Create course \t\t\t 2.Create data for student \n 3.Find course \t\t\t\t 4.Find student \n 5.print Courses List \t\t 6.print students List \n 7.after create both click to show all \n 8.Exit \n"))
    if x==1 :
        course_name=input("Enter course name : ")
        course_class=None
        while True:
            course_class = input("Enter course class (A\B\C) : ")
            if course_class in ["A","B","C"]:
                break

        course=Course(course_name,course_class)
        courses_list.append(course)
        print("course created successfuly ")
    elif x==2 :
        student_number=str(random.randint(1,10))
        student_name = input("Enter student name : ")
        while True:
            student_class = input("Enter student class (A\B\C) : ")
            if student_class in ["A", "B", "C"]:
                break

        student = Student(student_number, student_name, student_class)
        student_list.append(student)
        print("Data of student created successfuly ")
    elif x==3 :
        course_name=input("Enter course name : ")
        course_index = find_Course(course_name,courses_list)
        if course_index==-1:
            print("course Not exist !")
        else:
            print("name of course is ",courses_list[course_index].course_name,"\t\t\t","class of course is ",courses_list[course_index].course_class)
    elif x==4 :
        student_number = str(input("Enter student number : "))
        student_index = find_student(student_number, student_list)
        if student_index == -1:
            print("student Not exist !")
        else:
            print(" student number is ",student_list[student_index].student_number,"\n student name is ",
                  student_list[student_index].student_name, "\n student class is ",student_list[student_index].student_class)
    elif x == 5:
        print("---------------------------------")
        print("Course name \t\t Course class")
        print("---------------------------------")
        for i in courses_list:
            print(i.course_name, "\t\t\t\t", i.course_class)

    elif x==6 :
        print("---------------------------------------------------------")
        print("student number \t\t student name \t\t student Class")
        print("---------------------------------------------------------")
        for i in student_list:
            print(i.student_number, "\t\t\t\t\t", i.student_name, "\t\t\t\t\t", i.student_class)

    elif x==7:
         print("---------------------------------------------------------")
         print("student number \t\t student name \t\t student Class ")
         for i in student_list :
            print( i.student_number, "\t\t\t\t\t",i.student_name, "\t\t\t\t\t",  i.student_class)
         for i in courses_list:
             print("course name \t\t class course")
             print(i.course_name, "\t\t\t\t", i.course_class)
    elif x==8:
        exit()
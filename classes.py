from random import random
class Course :
    def __init__(self,course_name, course_class):
        self.course_name = course_name
        self.course_class = course_class

    def get_course_details (self):
        print('course name \t\t\t\t\t course class \n',self.course_name ,'\t\t\t\t\t',self.course_class)
class Student :

    def __init__(self,student_number,student_name,student_class):
     self.student_number = student_number
     self.student_name = student_name
     self.student_class = student_class
     self.courses_list=[]

    def add_course(self,course):
        if self.student_class == course.course_class:
            self.courses_list.append(course)
            print('Course Enrolled Successfully')
        else:
            print("Invalid Course Class")


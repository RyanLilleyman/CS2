# Project NO. 1
# Author: Ryan Lilleyman
# Description: This file contains the Student
# super class and its various methods and attributes.


from typing import Tuple
from typing_extensions import List


class Student:
    def __init__(self, name: str, credits: int):
        self.__name = name
        self.__credits = credits
        self.__course_list: List[Tuple] = []

    def getName(self):
        return self.__name

    def getCourseList(self):
        return self.__course_list

    def getCredits(self):
        return self.__credits

    def take_course(self, courseName: str, courseCredits: int):
        courseInfo = (courseName, courseCredits)
        self.__course_list.append(courseInfo)
        self.__credits += courseCredits

    def print_data(self):
        for course in self.__course_list:
            print(f"Course taken: {course[0]} ({course[1]} credits)")
        print(f"Credits completed {self.__credits}")

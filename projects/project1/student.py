# Project NO. 1
# Author: Ryan Lilleyman
# Description: This file contains the Student
# super class and its various methods and attributes.


from typing import Tuple
from typing_extensions import List


class Student:
    def __init__(self, name: str, id: int):
        self.__name = name
        self.__credits = 0
        self.__id = id
        self.__course_list: List[Tuple] = []

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def getCourseList(self):
        return self.__course_list

    def getCredits(self):
        return self.__credits

    def set_id(self, id: int):
        self.__id = id

    def set_name(self, name: str):
        self.__name = name

    def take_course(self, courseName: str, courseCredits: int):
        courseInfo = (courseName, courseCredits)
        self.__course_list.append(courseInfo)
        self.__credits += courseCredits

    def print_data(self):
        for course in self.__course_list:
            print(f"Course taken: {course[0]} ({course[1]} credits)")
        print(f"Credits completed {self.__credits}")

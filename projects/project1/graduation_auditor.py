# Project NO. 1
# Author: Ryan Lilleyman
# Description: This file contains the GraduationAuditor class and
# its various methods and attributes.


from grad_student import GradStudent
from undergrad_student import UndergradStudent


class GraduationAuditor:
    def __init__(self):
        self.__studentList = []

    def audit(self, list):
        self.__studentList = list
        for student in self.__studentList:
            if isinstance(student, UndergradStudent):
                if student.getCredits() >= 30 and student.get_communityService() >= 20:
                    print(f"{student.get_name()} can graduate")
                else:
                    print(f"{student.get_name()} cannot graduate")
            elif isinstance(student, GradStudent):
                if student.getCredits() >= 30 and student.get_publicationAmount() >= 2:
                    print(f"{student.get_name()} can graduate")
                else:
                    print(f"{student.get_name()} cannot graduate")

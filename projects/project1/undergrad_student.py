# Project NO. 1
# Author: Ryan Lilleyman
# Description: This file contains the UndergradStudent sub class and its various methods/ attributes

from student import Student


class UndergradStudent(Student):
    def __init__(self, name, courseCredits):
        super().__init__(name, courseCredits)
        self.__communityService = 0

    def do_community_service(self, hours: int):
        self.__communityService += hours

    def print_data(self):
        super().print_data()
        print(f"Hours of community service: {self.__communityService}")

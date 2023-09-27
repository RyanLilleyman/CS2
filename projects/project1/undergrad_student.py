# Project NO. 1
# Author: Ryan Lilleyman
# Description: This file contains the UndergradStudent sub class
# and its various methods/ attributes

from student import Student


class UndergradStudent(Student):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.__communityService = 0

    def get_communityService(self):
        return self.__communityService

    def set_communityService(self, hoursDone):
        self.__communityService = hoursDone

    def do_community_service(self, hours: int):
        self.__communityService += hours

    def print_data(self):
        super().print_data()
        print(f"Hours of community service: {self.__communityService}")

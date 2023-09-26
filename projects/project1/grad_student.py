# Project NO. 1
# Author: Ryan Lilleyman
# Description: This file contains the Student super
# class and its various methods and attributes.

from student import Student
from typing import List


class GradStudent(Student):
    def __init__(self, name: str, credit: int):
        super().__init__(name, credit)
        self.__publicationList: List[str] = []
        self.__numberofPubs: int = 0

    def publish_paper(self, paper: str):
        self.__publicationList.append(paper)
        self.__numberofPubs += 1

    def print_data(self):
        count = 0
        for item in self.__publicationList:
            count += 1
            print(f"Publication #{count}: {item}")
        super().print_data()
        print(f"Number of Publications: {self.__numberofPubs}")

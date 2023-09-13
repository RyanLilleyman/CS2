from os import name


class Person:
    def__init__(self, name, address, phoneNu):
        self.__name: name
        self.__address: address
        self.__phoneNu: phoneNu

    def setName(self,newName):
        self.__name: newName
    def setAddress(self,newAddress):
        self.__address: newAddress
    def setPhoneNu(self,newPhone):
        self.__phoneNu: newPhone
    

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def getPhoneNu(self):
        return self.__phoneNu



class Customer(Person):

    def __init__(self,name,address,phoneNu,cusNo,mailingList):
        super().__init__(name,address,phoneNu)
        self.__cusNo = cusNo
        self.__mailingList = mailingList

    def getCusNo(self):
        return self.__cusNo

    def getMailingList(self):
        return self.__mailingList

    def setCusNo(self,newCusNo):
        self.__cusNo = newCusNo

    def setMailingList(self,newMailingList):
        self.__mailingList = newMailingList

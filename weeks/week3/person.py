
class Person:
    def __init__(self, name, address, phone_no):
        self.__name = name
        self.__address = address
        self.__phone_no = phone_no

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_no(self):
        return self.__phone_no

class Customer(Person):
    def __init__(self, name, address, phone_no, cust_no, mailing_list):
        Person.__init__(self, name, address, phone_no)

        self.__cust_no = cust_no
        self.__mailing_list = mailing_list

    def set_cust_no(self, cust_no):
        self.__cust_no = cust_no

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_cust_no(self):
        return self.__cust_no

    def get_mailing_list(self):
        return self.__mailing_list

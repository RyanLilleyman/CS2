class Ticket:
    def __init__(self, name, date_of_birth, flight_number, miles):
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__flight_number = flight_number
        self.__miles = miles
        self.__type = type(self)
        self.discount_rate = 0
        self.ticket_cost = 0

    # getters
    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__date_of_birth

    def get_flight_number(self):
        return self.__flight_number

    def get_miles(self):
        return self.__miles

    def get_ticket_cost(self):
        return self.ticket_cost

    def get_type(self):
        return self.__type

    def get_discount_rate(self):
        return self.discount_rate

    # setters
    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__date_of_birth = dob

    def set_flight_number(self, fn):
        self.__flight_number = fn

    def set_miles(self, miles):
        self.__miles = miles

    def set_ticket_cost(self, miles, discount_rate):
        self.ticket_cost = miles * discount_rate

    def _set_discount_rate(self, rate):
        self.discount_rate = rate

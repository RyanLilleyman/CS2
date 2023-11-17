from ticket import Ticket


class Business(Ticket):
    def __init__(self, name, date_of_birth, flight_number, miles):
        super().__init__(name, date_of_birth, flight_number, miles)
        self._set_discount_rate()
        self.set_ticket_cost(self.get_miles(), self.discount_rate)

    def _set_discount_rate(self, rate=0.9):
        self.discount_rate = rate

    def set_ticket_cost(self, miles, discount_rate):
        self.ticket_cost = 5 * miles * discount_rate

    def get_type(self):
        return "Business"

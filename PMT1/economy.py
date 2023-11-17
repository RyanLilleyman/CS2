from ticket import Ticket


class Economy(Ticket):
    def __init__(self, name, date_of_birth, flight_number, miles):
        super().__init__(name, date_of_birth, flight_number, miles)
        self._set_discount_rate()
        self.set_ticket_cost(self.get_miles(), self.discount_rate)

    def _set_discount_rate(self, rate=0.95):
        self.discount_rate = rate

    def set_ticket_cost(self, miles, discount_rate):
        self.ticket_cost = miles * discount_rate

    def get_type(self):
        return "Economy"

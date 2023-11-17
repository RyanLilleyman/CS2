class Trips:
    def __init__(self):
        self.__total_travel_cost = 0
        self.__tickets = []

    def get_tickets(self):
        return self.__tickets

    def add_ticket(self, ticket):
        self.__tickets.append(ticket)

    def get_total_travel_cost(self):
        total = 0
        for ticket in self.__tickets:
            total += ticket.get_ticket_cost()
        return total

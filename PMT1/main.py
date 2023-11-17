from trips import Trips
from business import Business
from first_class import First
from economy import Economy


def main():
    trips = Trips()
    tick1 = Economy("Sonya Blade", "10/10/1977", "O4321", 140)
    tick2 = Business("Sub Zero", "1/1/1110", "O4322", 2240)
    tick3 = First("Liu Kang", "4/3/1964", "O4323", 420)
    tick4 = Business("Johnny Cage", "9/14/1981", "O4325", 703)
    tick5 = First("Scorpion", "4/5/1820", "O4326", 1234)
    tick6 = Business("Goro Goro", "4/1/1120", "O4327", 345)
    tick7 = Business("Reptile Reptile", "2/16/1102", "O4328", 3456)
    tick8 = First("Raiden Raiden", "7/15/1230", "O4329", 102354)
    tick9 = Business("Kano Kano", "4/5/1972", "O4344", 300)

    trips.add_ticket(tick1)
    trips.add_ticket(tick2)
    trips.add_ticket(tick3)
    trips.add_ticket(tick4)
    trips.add_ticket(tick5)
    trips.add_ticket(tick6)
    trips.add_ticket(tick7)
    trips.add_ticket(tick8)
    trips.add_ticket(tick9)

    print()
    print("Passengers Tickets")
    print("==================\n")
    print(
        f'{"Name":<18}{"DOB":<12}{"Flight":<8}{"# Miles":<8}{"Ticket Type":<13}{"Discount Rate":<15}{"Cost":^10}'
    )
    print(
        f'{"----":<18}{"---":<12}{"------":<8}{"-------":<8}{"-----------":<13}{"-------------":<15}{"----":^10}'
    )

    tickets = trips.get_tickets()

    for ticket in tickets:

        print(
            f"{ticket.get_name():<18}{ticket.get_dob():<12}{ticket.get_flight_number():<8}"
            f"{ticket.get_miles():<8}{ticket.get_type():<13}{ticket.get_discount_rate():^15,.2f}"
            f"{ticket.get_ticket_cost():>10,.2f}"
            
        )
        
        

    print()
    print(f'{"Total cost of tickets:   $"}{trips.get_total_travel_cost():>12,.2f}')
    print()


if __name__ == "__main__":
    main()

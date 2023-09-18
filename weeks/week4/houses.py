houses = ["Ewa's house", "Kevin's house", "Jen's house", "Tomaz's house", "Guido's house", "Audry's house"] 

# Each function call represents an elf doing his work 
def deliver_books_recursively(houses):
    # Worker elf doing his work
    if len(houses) == 1:
        house = houses[0]
        print("Delivering Learning Python textbook to", house)

    # Manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_books_recursively(first_half)
        deliver_books_recursively(second_half)

deliver_books_recursively(houses)

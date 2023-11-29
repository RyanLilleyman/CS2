'''
Lab PMT
By Ryan Lilleyman
Date: November 28th, 2023
'''

from farmapp import FarmApp
from livestock import Livestock
from alpaca import Alpaca
from camel import Camel
from donkey import Donkey


def main():
    farm = FarmApp()
    animal1 = Alpaca(5, 600) # Parameters:(int age, int weight)
    animal2 = Camel(5, 3) # Parameters: (int age, int numberOfHumps)
    animal3 = Donkey(6, "Miniature") # Parameters: (int age, String breed)
    farm.add_livestock(animal1)
    farm.add_livestock(animal2)
    farm.add_livestock(animal3)
    animals = farm.get_livestock()
    print("List of Animals Sold")
    print("====================\n")

    for animal in animals:
        print(f'{animal.get_animal_type():<10}{"$"}{animal.get_price():>12,.2f}')
    print()
    print(f'{"Total sales: "}{"$"}{farm.get_totoal_price():12,.2f}')
    animal4 = Donkey(2, "American Mammoth Jack") # Parameters: (int age, String breed)
    animal5 = Donkey(7, "Burro") # Parameters: (int age, String breed)
    animal6 = Alpaca(2, 250) # Parameters:(int age, int weight)
    farm.add_livestock(animal4)
    farm.add_livestock(animal5)
    farm.add_livestock(animal6)
    print()
    for animal in animals:
        print(f'{animal.get_animal_type():<10}{"$"}{animal.get_price():>12,.2f}')
    print()
    print(f'{"Total sales: "}{"$"}{farm.get_totoal_price():12,.2f}')

if __name__ == '__main__':
    main()

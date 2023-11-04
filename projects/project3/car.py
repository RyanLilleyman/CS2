class Car:
    """
    A class representing a car.

    Attributes:
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The price of the car.
        car_type (str): The type of the car.
    """

    def __init__(self, brand: str, model: str, year: int, price: float, car_type: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.car_type = car_type

import random
from car import Car


def main():
    car1Brand = "BMW"
    car1Color = "blue"
    car1MaxSpeed = random.randint(120, 200)
    car1Accel = random.randint(0, 10)

    car1 = Car(car1Brand, car1Color, car1MaxSpeed, car1Accel)

    car2Brand = "Mercedes"
    car2Color = "red"
    car2MaxSpeed = random.randint(120, 200)
    car2Accel = random.randint(0, 10)

    car2 = Car(car2Brand, car2Color, car2MaxSpeed, car2Accel)

    car3Brand = "Volvo"
    car3Color = "white"
    car3MaxSpeed = random.randint(120, 200)
    car3Accel = random.randint(0, 10)

    car3 = Car(car3Brand, car3Color, car3MaxSpeed, car3Accel)

    cars = [car1, car2, car3]

    for i in range(0, 3):
        print()
        print("For, ", cars[i])
        print("For, ", cars[i])
        print("Brand: ", cars[i].getBrand())
        print("Color: ", cars[i].getColor())
        print("MaxSpeed: ", cars[i].getMaxSpeed())
        print("Acceleration Rate: ", cars[i].getAccelerationRate())
        print("Current Speed: ", cars[i].getCurrentSpeed())
        print("Mile: ", cars[i].getMile())

    print()

    for i in range(0, 10):
        for car in cars:
            car.increaseSpeed()
            car.increaseMile()

    print()

    for i in range(0, 3):
        print()
        print("After the race, ", cars[i])
        print("Brand: ", cars[i].getBrand())
        print("Color: ", cars[i].getColor())
        print("MaxSpeed: ", cars[i].getMaxSpeed())
        print("Acceleration Rate: ", cars[i].getAccelerationRate())
        print("Current Speed: ", cars[i].getCurrentSpeed())
        print("Mile: ", cars[i].getMile())

    maximum = 0
    carThatWon = Car("", "", 0, 0)
    for car in cars:
        if car.getMile() > maximum:
            maximum = car.getMile()
            carThatWon = car

    print()
    print("Winner:")
    print(carThatWon.getBrand(), carThatWon.getMile())


if __name__ == "__main__":
    main()

class Car:
    def __init__(
        self,
        brand: str,
        color: str,
        maxSpeed: int,
        accelerationRate: int,
    ):
        self.brand = brand
        self.color = color
        self.maxSpeed = maxSpeed
        self.accelerationRate = accelerationRate
        self.currentSpeed = 0
        self.mile = 0

    def setBrand(self, brand: str):
        self.brand = brand

    def setColor(self, color: str):
        self.color = color

    def setMaxSpeed(self, maxSpeed: int):
        self.maxSpeed = maxSpeed

    def setCurrentSpeed(self, currentSpeed: int):
        self.currentSpeed = currentSpeed

    def increaseSpeed(self):
        self.currentSpeed += self.accelerationRate

    def increaseMile(self):
        self.mile += self.currentSpeed

    def getBrand(self) -> str:
        return self.brand

    def getColor(self) -> str:
        return self.color

    def getMaxSpeed(self) -> int:
        return self.maxSpeed

    def getCurrentSpeed(self) -> int:
        return self.currentSpeed

    def getAccelerationRate(self) -> int:
        return self.accelerationRate

    def getMile(self) -> float:
        return self.mile

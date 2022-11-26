from Car import Car

class uberPool(Car):
    brand = str
    model = str

    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model

    def printDataUberPool(self):
        super().printDataCar()
        print("Model: ", self.model)
        print("Brand: ", self.brand, "\n")
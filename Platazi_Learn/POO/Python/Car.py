from Account import Account

class Car:
    id          = int
    license     = str
    driver      = Account(str, str)
    passenger   = int

    def __init__(self, license, driver):
        self.license = license
        self.driver = driver

    def printDataCar(self):
        print('License: ', self.license)
        print('Driver Data: ', self.driver)
        print('Number of passenger: ', self.passenger)

    
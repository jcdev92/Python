from Car import Car
from Account import Account
from UberX import uberX
from UberPool import uberPool
from UberBlack import uberBlack
from UberVan import uberVan

#---------------------------------------------------------------- PRIMER SCRIPT PRACTICO DE CLASES EN PYTHON
#---------------------------------------------------------------- if __name__ == '__main__':              
#----------------------------------------------------------------     corolla = Car()
#----------------------------------------------------------------     corolla.license = 'AK7093'
#----------------------------------------------------------------     corolla.driver = 'Ramon Orlando'
#----------------------------------------------------------------     corolla.passenger = 5
#----------------------------------------------------------------     print(vars(corolla))
#---------------------------------------------------------------- 
#----------------------------------------------------------------     aveo = Car()
#----------------------------------------------------------------     aveo.license = 'JM0LK1'
#----------------------------------------------------------------     aveo.driver = 'Pedro Duque'
#----------------------------------------------------------------     aveo.passenger = 4
#----------------------------------------------------------------     print(vars(aveo))


#---------------------------------------------------------------- # SEGUNDO SCRIPT DE CLASES

#---------------------------------------------------------------- if __name__=='__main__':                                  
#----------------------------------------------------------------     Yaris = Car('RTM12I', Account("Ignacio Jose","k41jp23h"))
#----------------------------------------------------------------     print(vars(Yaris))
#----------------------------------------------------------------     print(vars(Yaris.driver))

#---------------------------------------------------------------- # TERCER SCROPT -- HERENCIAS

if __name__ == "__main__":
    spark = uberX('SA4521C5D', Account('Pedrito Fra', '18451912'), 'chevrolet', 'spark')
    spark.passenger = 4
    spark.printDataUberX()

    sedan = uberPool('215647L', Account('Pedro Sanchez', '8512961'), 'Nissan', 'Sedan')
    sedan.passenger = 3
    sedan.printDataUberPool()    
package Java;

public class Car {
    Integer id;
    private String license;
    private Account driver;
    protected Integer passenger;

    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    public Integer getPassenger(){ 
            return passenger;
    }

    void setPassenger(Integer passenger){
        if (passenger > 0 && passenger <= 4) {
            this.passenger = passenger;
        } else {
            System.out.println("\n");
            System.out.println("Solo pueden viajar de 1 hasta 4 pasajeros maximo, en este vehiculo");
        }

    }
    
    void printDataCar() {    
        if (passenger != null) {
            System.out.println("\n");
            System.out.println("License: " + license);
            System.out.println("Driver: " + driver.name);
            System.out.println("Passenger: " + passenger);
        }
    }
}

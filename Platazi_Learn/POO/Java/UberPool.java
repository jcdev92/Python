package Java;
class UberPool extends Car {
    String brand;
    String model;
    
    public UberPool(String license, Account driver, String brand, String model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;

    }

    @Override
    void printDataCar() {
        super.printDataCar();
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
    }

}
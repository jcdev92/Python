package Java;

import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;
    
    public UberVan(String license, Account driver) {
        super(license, driver);
  
    }

    public UberVan(String license, Account driver, Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }

    @Override
    void setPassenger(Integer passenger) {
        if (passenger > 0 && passenger <= 6) {
            this.passenger = passenger;
        } else {
            System.out.println("Solo pueden viajar de 1 hasta 6 pasajeros en maximo, en este vehiculo");
        }
    }

}

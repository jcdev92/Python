<?php

require_once ('car.php');

class UberVan extends Car{
    public $typeCarAccepted;
    public $seatsMaterial;

    public function __construct($license, $driver, $typeCarAccepted, $seatsMaterial){
        parent::__construct($license, $driver);
        $this->typeCarAccepted = $typeCarAccepted;
        $this->seatsMaterial = $seatsMaterial;
    }

    public function setPassengers($passengers) {
        if ($passengers > 0 && $passengers <= 6) {
            $this->passengers = $passengers;
        } else {
            echo "\nEl numero de pasajeros en este auto es de uno (1) a seis (6) pasajeros por viaje\n";
        }
    }

    function PrintDataUberVan() {
        parent::PrintDataCar();
        echo "    Marca: $this->typeCarAccepted 
        Modelo: $this->seatsMaterial
        ";
    }

}
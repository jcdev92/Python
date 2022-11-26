<?php

class Car {
public $id;
public $license;
public $driver;
protected $passengers;

function __construct($license, $driver) {
    $this->license = $license;
    $this->driver = $driver;
}

public function getPassengers() { 
    return $this->passengers;
}

public function setPassengers($passengers) {
    if ($passengers > 0 && $passengers <= 4) {
        $this->passengers = $passengers;
    } else {
        echo "\nEl numero de pasajeros en este auto es de uno (1) a cuatro (4) pasajeros por viaje\n";
    }
}

public function PrintDataCar() {
    if ($this->passengers != null) {
        echo "
        Licencia: $this->license 
        Driver: {$this->driver->name} 
        Número de pasajeros: $this->passengers
    ";
        }
    }
}
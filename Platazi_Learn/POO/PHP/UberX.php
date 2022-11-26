<?php

require_once ('car.php');

class UberX extends Car{
    public $brand;
    public $model;

    public function __construct($license, $driver, $brand, $model){
        parent::__construct($license, $driver);
        $this->brand = $brand;
        $this->model = $model;
    }
    function PrintDataUberX() {
        parent::PrintDataCar();
        echo "    Marca: $this->brand 
        Modelo: $this->model
        ";
    }
}
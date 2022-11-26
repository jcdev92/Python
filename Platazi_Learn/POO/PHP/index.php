<?php 

// ---------------------------------------------------------------- Primera practiva de clase con PHP DESACTIVADA

// ---------------------------------------------------------------- $car = new Car('AW456', new Account('Andres Herrera', 'AMS123'));
// ---------------------------------------------------------------- $car->printDataCar();


// ---------------------------------------------------------------- Ssegunda Practica Herencias con PHP ACTIVA

require_once('car.php');
require_once('UberX.php');
require_once('UberPool.php');
require_once('account.php');
require_once('UberVan.php');

$uberX = new UberX("QLK945", new Account("Andres Herrera", "M-26456891"), "Chevrolet", "Sparkline");
$uberX->setPassengers(4);
$uberX->printDataUberX();

$uberPool = new UberPool("KIJ251", new Account("Sarah Barrios", "E-88200145"), "Dodge", "Atittude");
$uberPool->setPassengers(3);
$uberPool->printDataUberPool();

$uberVan = new UberVan("KO2567J", new Account("Johny Mendoza", "M-35891234"), "Dodge", "Caravan");
$uberVan->setPassengers(6);
$uberVan->printDataUberVan();


?>

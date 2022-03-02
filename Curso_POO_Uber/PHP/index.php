<?php

require_once('Car.php');
require_once('uberX.php');
require_once('Account.php');

$car = new Car("AW456", new Account("Andres Herrera", "AMS123"));
$car->printDataCar();

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Sparks");
$uberX ->printDataCar();
?>
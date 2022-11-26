import Account from "./Account.js";
import Car from "./Car.js"
import uberX from "./UberX.js";

//  clases metodos y atributos 1

// test1 deshabilitado //  let PeterAcc = new Acc(14569, "Peter", 90851852, 'peter@gmail.com', 'peter2022');
// test1 deshabilitado //  console.log(PeterAcc);
// test1 deshabilitado //  console.log('  ');

//   clases atributos y metodos 2

// var Corolla = new car('','Corolla', "JUV35A", new Acc(4514, 'pedrito sanchez', 4512698, 'pedritocontigo@gmail.com', 'ped123', 'J14Q48-98', 0));
// Corolla.id = 'a2b5';
// Corolla.passenger = 5;
// 
// Corolla.printDataCar();

// Clasese metodos y atributos 3 -- Herencias

var yaris = new uberX("854695K", new Account('Paco Hernandez', 854695), "Toyota", "Yaris");

yaris.printDataCar();
yaris.printBrandModel();
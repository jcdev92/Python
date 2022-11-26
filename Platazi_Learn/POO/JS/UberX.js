import Car from "./Car.js";

class uberX extends Car {
    constructor(license, driver, brand, model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
    printBrandModel = () => {
        console.log('\n' + 'Brand: ' + this.brand);
        console.log('\n' + 'Model: ' + this.model);
    } 
}

export default uberX;
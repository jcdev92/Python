class Car { 
    constructor(license, driver) {
        this.id;
        this.license = license;                       // string
        this.driver = driver;
        this.passenger;
    }
    printDataCar = () => {
        console.log('\n' + 'License: ' + this.license);
        console.log('\n' + 'Driver Data : ');
        console.log(this.driver);
    } 
}

export default Car;
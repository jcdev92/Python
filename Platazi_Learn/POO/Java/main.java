package Java;

class Main {
    public static void main(String[] args) {
        UberX chevy = new UberX("KIO291", new Account("Carlitos Duran", "2585123"), "Chevrolet", "Chevy");
        // chevy.passenger = 4; 
        chevy.setPassenger(3);
        chevy.printDataCar();
        

        UberPool patrol = new UberPool("LP012I", new Account("Eusebio Sacristan", "6185796"),"Nissan", "Patrol");
        // patrol.passenger = 3;
        patrol.setPassenger(2);
        patrol.printDataCar();

        UberVan previa = new UberVan("KLH054", new Account("Dross Lam", "11590124"));
        // previa.passenger = 3;
        previa.setPassenger(6);
        previa.printDataCar();
        
    }
}
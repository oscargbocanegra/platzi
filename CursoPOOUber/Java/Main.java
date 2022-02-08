package github.platzi.CursoPOOUber.Java;

class Main {
    public static void main(String[] args) {
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123", "andres21mail.com", "qwe546"), "prueba", "prueba");
        uberX.setPassenger(4);
        uberX.printDataCar();

        UberVan uberVan = new UberVan("AMQ789", new Account("Andres Lopez","AND2587"));
        uberVan.setPassenger(6);
        uberVan.printDataCar();
    }
}
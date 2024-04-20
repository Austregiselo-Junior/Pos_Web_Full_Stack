package br.unipe.boaspraticas.exercicios.solid.srp;

public class CalculatorFromItem {

    public void calculateTotalPrice() {

        Order order = new Order();
        double total = 0;
        for (Item item : order.getItems()) {
            total += item.ItemQuantity();
        }
        System.out.println("Total Price: " + total);
    }
}

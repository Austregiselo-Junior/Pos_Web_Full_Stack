package br.unipe.boaspraticas.exercicios.solid.srp;

import java.util.List;

public class Order {
    private int orderId;
    private String customerName;
    private List<Item> items;

    public Order(){}

    public Order(int orderId, String customerName, List<Item> items) {
        this.orderId = orderId;
        this.customerName = customerName;
        this.items = items;
    }

    public List<Item> getItems(){
        return items;
    }
}

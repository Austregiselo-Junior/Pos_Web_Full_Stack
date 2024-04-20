package br.unipe.boaspraticas.exercicios.oc;
import br.unipe.boaspraticas.exercicios.solid.model.Item;

import java.util.ArrayList;
import java.util.List;

public class ShoppingCart { // Essa classe tem várias responsabilidades
    private List<Item> items;

    public ShoppingCart() {
        items = new ArrayList<>();
    }

    public void addItem(Item item) {
        items.add(item);
    }

    public void removeItem(Item item) {
        items.remove(item);
    }

    public void calculateTotalPrice() {

        double totalPrice = 0;

        for (Item item : items) {
            totalPrice += item.getPrice(); // Mais de um nível de identação
        }
        System.out.println("Total Price: " + totalPrice);
    }

    public void printItems() {
        for (Item item : items) {
            System.out.println(item.getNome() + " - $" + item.getPrice());
        }
    }

    public void saveToDatabase() { // pode ser um serviço externo a essa classe
        // Lógica para salvar o carrinho de compras no banco de dados
    }

    public void sendConfirmationEmail() {  // pode ser um serviço externo a essa classe
        // Lógica para enviar um e-mail de confirmação do carrinho de compras
    }
}
package br.unipe.boaspraticas.exercicios.oc;


// Identifique quais são as regras que , neste exemplo, a classe Customer não segue em relação a Object Calisthenics:
// Antes de olhar o arquivo texto com as respostas, tente descrever o que você identificou.
public class Customer { // Classe deve ser pequena e com uma única responsabilidade

    private String name; // Aqui pode usar classes em vez de setar a variável primitiva
    private int age;
    private double totalPurchaseAmount; //

    public Customer(String name, int age) {
        this.name = name;
        this.age = age;
        this.totalPurchaseAmount = 0;
    }

    // Getters e Setters

    public void addToTotalPurchaseAmount(double amount) {
        this.totalPurchaseAmount += amount;
    }

    public void makePurchase(double amount) {
        if (amount > 0) {
            addToTotalPurchaseAmount(amount);
            System.out.println("Purchase successful!");
            if (age >= 18) { // Evitar vários if e identação desnecessária, isso poderia ser um método
                sendEmailReceipt(amount);
            }
        } else { // Não usar else
            System.out.println("Invalid purchase amount!");
        }
    }

    public void sendEmailReceipt(double amount) {
        // Lógica para enviar um e-mail com o recibo da compra
        System.out.println("Email receipt sent. Amount: " + amount); // isso poderia está numa classe específica.
    }
}

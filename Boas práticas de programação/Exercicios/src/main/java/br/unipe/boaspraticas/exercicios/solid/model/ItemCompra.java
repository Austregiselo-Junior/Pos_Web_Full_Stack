package br.unipe.boaspraticas.exercicios.solid.model;


import lombok.Data;

@Data
public class ItemCompra {
    private String nome;  //NOME da pessoa realizando compra
    private double preco; //Preço da compra
    private int quantidade;  // Quantidade de itens

    public double getPreco(){
        return preco;
    }

    public int getQuantidade(){
        return getQuantidade();
    }

}

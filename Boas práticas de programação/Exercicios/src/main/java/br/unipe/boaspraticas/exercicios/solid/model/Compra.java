package br.unipe.boaspraticas.exercicios.solid.model;

import lombok.Data;

import java.util.List;

@Data
public class Compra {
    private List<ItemCompra> itens;   //Lista de itens
    private double desconto; //desconto a ser aplicado

    public double getDesconto(){ return desconto;}
    public List<ItemCompra> getItnes(){ return itens;}

    // getters e setters omitidos
}

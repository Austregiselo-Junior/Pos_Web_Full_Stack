package br.unipe.boaspraticas.exercicios.solid.ocp;

import br.unipe.boaspraticas.exercicios.solid.model.Compra;
import br.unipe.boaspraticas.exercicios.solid.model.ItemCompra;

// Classe responsável por calcular o valor total de uma compra
public class CalculadoraDeCompra {
    public double calcularTotal(Compra compra) {
        double total = 0;
        for (ItemCompra item : compra.getItnes()) {
            total += item.getPreco() * item.getQuantidade();
        }
        if (compra.getDesconto() > 0) {
            total -= total * (compra.getDesconto() / 100);
        }
        return total;
    }
}



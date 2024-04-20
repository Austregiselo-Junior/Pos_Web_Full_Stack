package br.unipe.boaspraticas.exercicios.solid.ocp.formas;

import br.unipe.boaspraticas.exercicios.solid.ocp.CalcularArea;

public class Retangulo implements CalcularArea {

    private double altura;
    private double largura;


    @Override
    public double calcularArea() {
        return altura * largura;
    }
}

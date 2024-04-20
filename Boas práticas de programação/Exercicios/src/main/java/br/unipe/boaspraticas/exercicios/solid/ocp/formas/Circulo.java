package br.unipe.boaspraticas.exercicios.solid.ocp.formas;
import br.unipe.boaspraticas.exercicios.solid.ocp.CalcularArea;

public class Circulo implements CalcularArea {

    private double raio;

    @Override
    public double calcularArea() {
        return Math.PI * raio * raio;
    }
}

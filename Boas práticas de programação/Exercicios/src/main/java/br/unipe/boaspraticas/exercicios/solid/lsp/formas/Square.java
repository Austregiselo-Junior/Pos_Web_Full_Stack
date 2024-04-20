package br.unipe.boaspraticas.exercicios.solid.lsp.formas;

class Square implements Shape {
    private int side;

    public void setSide(int side) {
        this.side = side;
    }

    @Override
    public double getArea() {
        return side * side;
    }
}
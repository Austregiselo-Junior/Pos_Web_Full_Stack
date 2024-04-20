package br.unipe.boaspraticas.exercicios.solid.lsp.pessoas;

class Funcionario extends Pessoa implements FazerSom{

    private double salario;

    public Funcionario(String nome, double salario) {
        super(nome);
        this.salario = salario;
    }

    public double getSalario() {
        return salario;
    }

    // Método específico da classe Funcionario
    public void calcularSalario() {
        // Lógica para calcular o salário do funcionário
    }

    @Override
    public void fazerSom() {
        super.fazerSom();
        System.out.println("Bom dia!");
    }


}

package br.unipe.boaspraticas.exercicios.solid.lsp.pessoas;

public class LiskovExample {
    public static void main(String[] args) {

        Pessoa pessoa = new Funcionario("João", 3000);
        pessoa.fazerSom();


        Funcionario funcionario = new Funcionario("Maria", 500);
        funcionario.fazerSom();
    }
}

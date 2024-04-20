package br.unipe.boaspraticas.exercicios.solid.sip.trabalhadores;

class Estagiario implements Trabalhador {
    @Override
    public void trabalharEmTempoIntegral() {
        // Implementação do trabalho em tempo integral para um estagiário
        System.out.println("Estagiário trabalhando em tempo integral.");
    }

    @Override
    public void fazerTrabalhoTemporario() {
        // Implementação do trabalho temporário para um estagiário
        System.out.println("Estagiário também faz trabalhos temporários.");
    }
}

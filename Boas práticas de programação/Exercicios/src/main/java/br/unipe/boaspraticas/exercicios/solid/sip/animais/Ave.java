package br.unipe.boaspraticas.exercicios.solid.sip.animais;

class Ave implements AnimalVoador, Animal {
    @Override
    public void comer() {
        System.out.println("A ave está comendo.");
    }

    @Override
    public void dormir() {
        System.out.println("A ave está dormindo.");
    }

    @Override
    public void voar() {
        System.out.println("A ave está voando.");
    }


}

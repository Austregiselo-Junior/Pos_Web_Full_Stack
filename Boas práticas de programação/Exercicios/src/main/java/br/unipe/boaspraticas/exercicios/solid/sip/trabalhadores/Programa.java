package br.unipe.boaspraticas.exercicios.solid.sip.trabalhadores;



//Neste exemplo, a interface Trabalhador contém dois métodos, um para trabalhar em tempo integral e outro para
// fazer um trabalho temporário. A classe Gerente implementa essa interface e fornece implementações
// para ambos os métodos. No entanto, a classe Estagiario também implementa a mesma interface, e isso pode violar o ISP.

//A violação do ISP ocorre porque a classe Estagiario é forçada a implementar o método fazerTrabalhoTemporario(),
// mesmo que isso não faça sentido para um estagiário. Isso pode levar a código desnecessário ou implementações
// vazias em algumas classes, o que não é ideal.
class Programa {
    public static void main(String[] args) {
        Trabalhador gerente = new Gerente();
        gerente.trabalharEmTempoIntegral();
        gerente.fazerTrabalhoTemporario();

        Trabalhador estagiario = new Estagiario();
        estagiario.trabalharEmTempoIntegral();
        estagiario.fazerTrabalhoTemporario();
    }
}

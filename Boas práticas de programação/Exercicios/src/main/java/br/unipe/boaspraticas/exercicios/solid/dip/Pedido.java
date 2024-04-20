package br.unipe.boaspraticas.exercicios.solid.dip;

class Pedido {
    private DataBaseService _dataBaseService;

    public Pedido(DataBaseService dataBaseService) {
        _dataBaseService = dataBaseService;
    }

    public void salvar() {
        _dataBaseService.SalvarPedido();
    }
}

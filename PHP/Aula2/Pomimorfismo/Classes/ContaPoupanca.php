<?php
    final class ContaPoupanca extends Conta
    {
        public function imprimirExtrato(){
        echo "Extrato da conta poupança <br/>";
        echo "Saldo:" . $this->saldo . "<br/>";
    }
    }
    
?>
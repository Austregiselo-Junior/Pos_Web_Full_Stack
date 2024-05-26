<?php

class Conta
{
     protected $saldo;

     public function getSaldo()
     {
          return $this->saldo;
     }

     public function setSaldo($saldo)
     {
          $this->saldo = $saldo;
          return $this;
     }

    public function depositar($quantia){
        $this->saldo += $quantia;
    }

    public function sacar($quantia){
        if($this->saldo <= 0 || $this->saldo < $quantia){
            echo "Não pode sacar, conta zerada!";
        }
        else{
               $this->saldo -= $quantia;
        }
    }

    public function imprimirExtrato(){
        echo "Extrato: <br/>";
        echo "Saldo:" . $this->saldo . "<br/>";
    }
}
?>
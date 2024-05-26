<?php
    final class ContaCorrente extends Conta
    {
      public function sacar($quantia){
             if($this->saldo <= 0 || $this->saldo < $quantia){
              echo "Não pode sacar, conta zerada!";
           }
           else{
                  $this->saldo -= $quantia + 0.1;
           }
       }

       public function imprimirExtrato(){
        echo "Extrato da conta corrente <br/>";
        echo "Saldo:" . $this->saldo . "<br/>";
    }
        
    }
    
?>
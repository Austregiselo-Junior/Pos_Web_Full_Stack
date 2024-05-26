<?php
     namespace Classes;
     class Programador extends Funcionario{
        private $linguagem;

        public function __construct($nome, $salario, $obs){ 
                $this->linguagem = $obs;
                parent::__construct($nome, $salario);
        }

        public function getLinguagem()
        {
                return $this->linguagem;
        }

        public function setLinguagem($linguagem)
        {
                $this->linguagem = $linguagem;

                return $this;
        }

        public function relatorioFunc() {
            echo $this->nome . "<br/>";
            echo $this->salario . "<br/>";
            echo $this->linguagem . "<br/>";
        }
    }
    
?>
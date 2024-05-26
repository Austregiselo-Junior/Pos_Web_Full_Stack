<?php
    namespace Classes;
    class Funcionario{
        protected $nome;
        protected $salario;

        public function __construct($nome, $salario){
             $this->nome = $nome;
             $this->salario = $salario;
        }

        public function __destruct(){
            echo "Vc está bem!";
        }

        public function relatorioFunc() {
            echo $this->nome . "<br/>";
            echo $this->salario . "<br/>";
        }

        public function getNome()
        {
                return $this->nome;
        }

        public function setNome($nome)
        {
                $this->nome = $nome;

                return $this;
        }
    }
?>
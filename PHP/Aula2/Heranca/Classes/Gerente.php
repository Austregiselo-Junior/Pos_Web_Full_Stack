<?php
    namespace Classes;
    class Gerente extends Funcionario{
        private $Projeto;

          public function __construct($nome, $salario, $obs){ 
                $this->projeto = $obs;
                parent::__construct($nome, $salario);
        }

        public function getProjeto()
        {
                return $this->Projeto;
        }

        public function setProjeto($Projeto)
        {
                $this->Projeto = $Projeto;

                return $this;
        }

        public function relatorioFunc() {
            echo $this->nome . "<br/>";
            echo $this->salario . "<br/>";
            echo $this->Projeto . "<br/>";
        }
    }
?>
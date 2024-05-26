<?php
     class Produto {
        public $codigo;
        public $descricao;
        public $preco;
        public $quantidade;

        public function __construct($codigo, $descricao, $preco, $quantidade){
            $this->codigo = $codigo;
            $this->descricao = $descricao;
            $this->preco = $preco;
            $this->quantidade = $quantidade;
        }

        public function __destruct(){
            echo "Tchau";
        }

        public function imprimeRelatorio() {
            echo "Código: {$this->codigo} <br/>";
            echo "Descrição: {$this->descricao} <br/>";
        }
    }
?>
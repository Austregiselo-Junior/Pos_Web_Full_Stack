<?php
    require_once "Classes/Conta.php";
    require_once "Classes/ContaPoupanca.php";
    require_once "Classes/ContaCorrente.php";


    $contaCorrente = new ContaCorrente();
    $contaPoupanca = new ContaPoupanca();

    $contaCorrente->setSaldo(200);
    $contaPoupanca->setSaldo(200);

    $contaCorrente->sacar(100);
    $contaPoupanca->sacar(100);

    $contaCorrente->imprimirExtrato();
    $contaPoupanca->imprimirExtrato();

?>
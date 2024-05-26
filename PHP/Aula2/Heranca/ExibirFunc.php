<?php
    require_once "autoload.php";

    use Classes\Funcionario;
    use Classes\Gerente;
    use Classes\Programador;

    $nome = $_POST['Nome'];
    $salario = $_POST['Salario'];
    $cargo = $_POST['Cargo'];
    $OBS = $_POST['OBS'];

    $funcionario = null;

    if($cargo == 0){
        $funcionario = new Programador($nome, $salario);
      //  $funcionario->setLinguagem($OBS);
    }
    else{
        $funcionario = new Gerente($nome, $salario);
       // $funcionario->setProjetp($OBS);
    }
    $funcionario->relatorioFunc($OBS);

?>
<?php
    $servidor = new PDO("mysql:host=localhost:3306;dbname=aula3","root",""); // Criando consualta
    $servidor->exec("Insert into famosos (nome) values ('Austregíselo')"); // execultar consulta
    $tabela =  $servidor->query("Select id,nome from famosos"); // execultar consulta


    if($tabela){
        foreach($tabela as $linha){
         echo $linha['id'] . "-" . $linha['nome'] . "<br/>";
         }
    }
    // Consultas preparadas usando Cash de memória
      $nome = "Austregíselo";
      $consulta = $servidor->prepare("Insert into famosos (nome) values (:nome)"); // preparando uma consulta
      $consulta->bindParam(':nome', $nome); // Fazendo filtro de campo, evita injeção de código aumentando a segurança

      $consulta->execute();

      $nome = "André";
      $consulta->execute();
    $servidor = null;
?>
<?php
	// POST, porque tem que ser o mesmo tipo usado no método, do formulario.html, ou pode usar o REQUEST que é genérico
	$nome = $_POST["nome"];

	echo "bem vindo, $nome";
	echo "<br/><a href='formulario1.html'>Voltar</a>";
?>
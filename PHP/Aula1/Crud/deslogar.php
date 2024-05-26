<?php
	//setcookie('logado', 0);// Validação com cookie
	
	session_start();
	$_SESSION['logado'] = 0;
	header('Location:index.php');
?>
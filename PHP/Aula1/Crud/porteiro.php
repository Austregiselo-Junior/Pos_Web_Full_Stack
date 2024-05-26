<?php
	session_start();

	$login = $_POST['login'];
	$senha = $_POST['senha'];
	
	$servidor = mysqli_connect("localhost", "root", "", "torcedores");
	
	$tabela = mysqli_query($servidor, "select * from usuario where login='$login' and senha='$senha'");
	
	if(mysqli_num_rows($tabela)>0){
			//setcookie("logado", 1);// Validação com cookie
			$_SESSION['logado'] = 1;
			header("location: dashboard.php");
	}else{
			$_SESSION['logado'] = 0;
			//setcookie("logado", 0);// Validação com cookie
			header("location: index.php");
	}
?>
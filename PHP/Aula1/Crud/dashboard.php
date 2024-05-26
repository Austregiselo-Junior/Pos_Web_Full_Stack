<?php
	session_start();

	if($_SESSION['logado'] == 1){// Validação com cookie por no if ($_COOKIE['logado'] == 1)
		echo "Logado! <a href='deslogar.php'>Logout</a>";
	}
	else
		header("Location: index.php");
?>
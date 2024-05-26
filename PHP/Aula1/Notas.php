<?php
	$nome = $_POST["nome"];
	$nota1 = $_POST["nota1"];
	$nota2= $_POST["nota2"];
	
	$media = ($nota1 + $nota2)/2;
	
	if($media >= 7){
		echo "O aluno $nome teve media $media, está aprovado.";
		
	}
	 else {
		 echo "O aluno $nome teve media $media, está reprovado.";
	 }	 
?>
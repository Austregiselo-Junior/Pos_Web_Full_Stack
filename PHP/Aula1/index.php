

<?php
// comentario em linha

/*
 comentario em bloco
*/

 $nome = "Austregiselo";
 $peso = 80.5;
 $bool = false;
 
  // strings e concatenação
	echo "Hello Sr ". $nome . "<br/>";
	echo "<b>Hello Sr $nome</b>";
 
 // Arrays
	// numérico
	$carros = array("Fusca", "Fiat", "Ferrati");
	echo $carros[1];
	
	//Associativos
	$idades = array("Astro"=>34, "Teo"=>8);
	echo $idades["Teo"] . "<br/>";
 
	// multidimensional
	$times = array(
		"PB" => array("Sousa","Belo","Treze"),
		"PE" => array("Sport","Retro","Barbie"),
		"SP" => array("Sao Paulo","Palmeiras","Corinthias")
	);
	echo $times["PE"][1] . "<br/>";
	
	
	// Conectar com o MySQL e selecinar um DB, URL:localhost/phpmyadmin
	$servidor = mysqli_connect("localhost","root","","aula1");
	
	
	// fazer a consualta sqlite_array_query, onde o primeiro parâmetro é o local e o segundo é a consulta
		// Add valor no DB:
			//mysqli_query($servidor, "Insert into cadastro (nome,telefone) value ('Austregiselo','83998905014')");
		
		// Fazer consulta e mostrar numa tabela
			$tabela = mysqli_query($servidor, "SELECT * FROM cadastro");
	
		echo "
			<table border=1>
			<tr>
				<td>NOME</td>
				<td>TELEFONE</td>
			</tr>
			";
	
		while($linha = mysqli_fetch_array($tabela)) {
			echo "<tr>";
			echo "<td>" . $linha['nome'] . "</td>";
			echo "<td>" . $linha['telefone'] . "</td>";
			echo "</tr>";
		}
	
		echo "
			</table>
		";
 
 
	// OBS: Fechar conecxão
	mysqli_close($servidor);
	
	// Para deletar linha da tabela
	$DeletarCampo = mysqli_query($servidor, "Delete FROM cadastro where id=1");
	
?>
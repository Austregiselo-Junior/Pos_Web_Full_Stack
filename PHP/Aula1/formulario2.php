<html>
	<body>
		<h1> Boas vindas </h1>
		
		<form method="POST">
			<p>
				Nome:	<input type="text" name="nome" />
			</p>
		</form>
		
		<p>
			<?php
				if($_SERVER["REQUEST_METHOD"] == "POST")
				{
					$nome = $_POST["nome"];
					echo "bem vindo, $nome";
				}
				
			
			?>
		</p>
	</body>
</html>
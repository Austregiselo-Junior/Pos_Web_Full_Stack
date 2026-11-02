CREATE TABLE IF NOT EXISTS treinamento_coii.teste_hdp (
		id INT COMMENT 'Id de teste.',
		nome STRING COMMENT 'Nome de teste.',
		data_nascimento DATE COMMENT 'Data de nascimento de teste.',
		valor_salario DECIMAL(9 , 2) COMMENT 'Valor do salário de teste.'
	) 
	COMMENT 'Tabela de teste'
	STORED AS ORC;
	
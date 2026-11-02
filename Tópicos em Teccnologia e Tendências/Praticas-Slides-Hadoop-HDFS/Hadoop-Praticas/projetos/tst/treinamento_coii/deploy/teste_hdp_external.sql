CREATE EXTERNAL TABLE IF NOT EXISTS stg_treinamento_coii.ex_teste_hdp (
		id STRING COMMENT 'Id de teste.',
		nome STRING COMMENT 'Nome de teste.',
		data_nascimento STRING COMMENT 'Data de nascimento de teste.',
		valor_salario STRING COMMENT 'Valor do salário de teste.'
	) 
	COMMENT 'Tabela de teste'
	ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
	WITH SERDEPROPERTIES (
		"separatorChar" = "\u003B",
		"quoteChar"     = "\"",
		"escapeChar"    = "\\"
	);

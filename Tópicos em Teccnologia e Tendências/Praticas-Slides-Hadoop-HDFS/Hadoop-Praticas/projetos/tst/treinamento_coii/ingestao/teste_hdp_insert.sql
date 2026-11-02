INSERT OVERWRITE TABLE treinamento_coii.teste_hdp
SELECT 
id,
nome,
to_date(from_unixtime(unix_timestamp(data_nascimento, 'yyyyMMdd'))),
valor_salario 
FROM stg_treinamento_coii.ex_teste_hdp;

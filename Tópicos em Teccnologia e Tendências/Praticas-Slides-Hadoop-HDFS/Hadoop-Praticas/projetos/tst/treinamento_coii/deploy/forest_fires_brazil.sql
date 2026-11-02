CREATE EXTERNAL TABLE IF NOT EXISTS stg_treinamento_coii.ex_forest_fires_brazil (
		year STRING COMMENT 'Year when Forest Fires happen',
		state STRING COMMENT 'Brazilian State',
		month STRING COMMENT 'Month when Forest Fires happen',
		number STRING COMMENT 'Number of Forest Fires reported',
		date_report STRING COMMENT 'Date when Forest Fires where reported'
	) 
	COMMENT 'This dataset report of the number of forest fires in Brazil divided by states. The series comprises the period of approximately 10 years (1998 to 2017). By Kaggle @gustavomodelli'
	ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
	WITH SERDEPROPERTIES (
		'separatorChar' = ',',
		'quoteChar'     = '\"'
	)
	TBLPROPERTIES 
	(
		'skip.header.line.count'='1'
	);


CREATE TABLE IF NOT EXISTS treinamento_coii.forest_fires_brazil (
		year INT COMMENT 'Year when Forest Fires happen',
		state STRING COMMENT 'Brazilian State',
		month STRING COMMENT 'Month when Forest Fires happen',
		number INT COMMENT 'Number of Forest Fires reported',
		date_report DATE COMMENT 'Date when Forest Fires where reported'
	) 
	COMMENT 'This dataset report of the number of forest fires in Brazil divided by states. The series comprises the period of approximately 10 years (1998 to 2017). By Kaggle @gustavomodelli'
	STORED AS ORC;

INSERT OVERWRITE TABLE treinamento_coii.forest_fires_brazil
SELECT 
year,
upper(trim(state)),
upper(trim(month)),
number,
date_report
FROM stg_treinamento_coii.ex_forest_fires_brazil;
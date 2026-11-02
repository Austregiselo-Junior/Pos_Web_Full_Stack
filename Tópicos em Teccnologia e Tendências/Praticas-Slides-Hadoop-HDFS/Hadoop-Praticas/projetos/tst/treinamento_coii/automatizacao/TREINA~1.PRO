# configurações Ambiente
oozie.wf.validate.ForkJoin=false
oozie.use.system.libpath=true
dfs.namenode.kerberos.principal.pattern=*
jobTracker=172.18.0.2:8032
nameNode=hdfs://sandbox-hdp.hortonworks.com:8020
jdbcUrl=jdbc:hive2://sandbox-hdp.hortonworks.com:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2
hivePrincipal=hive/_HOST@EXAMPLE.COM
diretorioAutomatizacao=/user/maria_dev/scripts_eder/treinamento_coii/automatizacao
diretorioScripts=/user/maria_dev/scripts_eder/treinamento_coii/ingestao
diretorioDados=/user/maria_dev/scripts_eder/treinamento_coii/dados
diretorioETL=/user/maria_dev/scripts_eder/treinamento_coii/etl
fetchSize=100000

# configurações do BD
stringBanco=jdbc:oracle:thin:@e1112-dscan2.exadata.prevnet:1521:ddc
usuario=SDC_INTRANET
senha=SDC_INTRANET00

# Configurações para envio do e-mail
destinatariosNotificacoes=eder.nogueira@dataprev.gov.br
ccNotificacoes=eder.nogueira@dataprev.gov.br

# Dados gerais
cliente=tst
database=treinamento_coii

# Tabela municipios
tabelaMunicipios=municipios
sqlImportacaoMunicipios=SELECT MUNICIPIOS.ID_MUNI_PREV, MUNICIPIOS.NU_MUNI_IBGE, MUNICIPIOS.NU_MUNI_SERPRO, MUNICIPIOS.NM_MUNI, MUNICIPIOS.NU_CEP, MUNICIPIOS.ID_MUNI_ECT, MUNICIPIOS.IN_NOME_MUN_IGUAL, MUNICIPIOS.SG_UF STRING, MUNICIPIOS.IN_MAP, MUNICIPIOS.ID_REGIAO_METROPOLITANA, MUNICIPIOS.NU_DDD, MUNICIPIOS.QT_POPULACAO, MUNICIPIOS.DT_INIC_VALI, MUNICIPIOS.ID_MESORREGIAO, MUNICIPIOS.ID_UF_PREV, MUNICIPIOS.NU_LATITUDE, MUNICIPIOS.NU_LONGITUDE FROM SDC.TB0008 MUNICIPIOS WHERE $CONDITIONS
splitByMunicipios=ID_MUNI_PREV
stagingAreaMunicipios=/dados/staging_area/tst/treinamento_coii/ex_municipios

# Tabela teste_hdp
tabelaTesteHdp=teste_hdp
stagingAreaTesteHdp=/dados/staging_area/tst/treinamento_coii/ex_teste_hdp
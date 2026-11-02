INSERT OVERWRITE TABLE TREINAMENTO_COII.MUNICIPIOS
SELECT 
    TRANSLATE(ID_MUNI_PREV ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    TRANSLATE(NU_MUNI_IBGE ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    TRANSLATE(NU_MUNI_SERPRO ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    upper(trim(NM_MUNI)),
    TRANSLATE(NU_CEP ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    TRANSLATE(ID_MUNI_ECT ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    trim(IN_NOME_MUN_IGUAL),
    upper(trim(SG_UF)),
    trim(IN_MAP),
    trim(ID_REGIAO_METROPOLITANA),
    trim(NU_DDD),
    TRANSLATE(QT_POPULACAO ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    IF(DT_INIC_VALI = '00000000', NULL, to_date(from_unixtime(unix_timestamp(DT_INIC_VALI, 'dd/MM/yyyy hh:mm:ss')))),
    TRANSLATE(ID_MESORREGIAO ,'\ \.\:\/\@\#\$\%\&\*\(\)\_\-\+\=\§\`\[\{\ç\Ç\~\^\]\}\|\,\<\\', ''),
    trim(ID_UF_PREV),
    NU_LATITUDE,
    NU_LONGITUDE
FROM STG_TREINAMENTO_COII.EX_MUNICIPIOS;

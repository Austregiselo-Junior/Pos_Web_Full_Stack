<?php
    require_once "Produto.php";

    $cd = new Produto(1, "CD-ROM", 200, 34);
    $cd->imprimeRelatorio();
?>
<?php
/* get https://api.labelary.com/v1/barcodes?{parameters} */

require_once '../config/conector.php';

$dados = $pdo->prepare('SELECT pyt_id, pyt_nome, pyt_telefone, pyt_email, pyt_nascimento, pyt_observacoes
                         FROM tb_python_api');
$dados->execute();
$dadosOk = $dados->fetchAll(PDO::FETCH_ASSOC);

echo json_encode($dadosOk);
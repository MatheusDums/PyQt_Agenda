<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector.php';

$listar = $pdo->query('SELECT `pyt_id`,`pyt_nome`, `pyt_telefone`, `pyt_email`, `pyt_nascimento`, `pyt_observacoes` FROM tb_python_api');
$dados = $listar->fetchAll(PDO::FETCH_ASSOC);

echo json_encode($dados);
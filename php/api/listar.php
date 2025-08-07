<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector.php';
require_once '../config/conector_login.php';

$stmt = $pdo->prepare('SELECT pyt_token FROM tb_python_login');
$stmt->execute();
$dados = $stmt->fetchAll(PDO::FETCH_ASSOC);
$token_ok = $dados[0]['pyt_token'];


$listar = $pdo->query('SELECT `pyt_id`,`pyt_nome`, `pyt_telefone`, `pyt_email`, `pyt_nascimento`, `pyt_observacoes` FROM tb_python_api');
$dados = $listar->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($dados);
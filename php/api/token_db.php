<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector_login.php';

$stmt = $pdo->prepare('SELECT pyt_token FROM tb_python_login');
$stmt->execute();
$dados = $stmt->fetchAll(PDO::FETCH_ASSOC);

echo json_encode($dados[0]['pyt_token']);
?>
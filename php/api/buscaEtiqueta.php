<?php
require_once '../config/conector.php';

$dados_buscar = file_get_contents('php://input');

$dados_log = json_decode($dados_buscar, true);

$codigo = $dados_log['codigo'];

$listar = $pdo->prepare('SELECT `pyt_id`,`pyt_nome`, `pyt_telefone`, `pyt_email`, `pyt_nascimento`, `pyt_observacoes` 
                        FROM tb_python_api WHERE pyt_telefone = :codigo LIMIT 1');
$listar->bindParam(':codigo', $codigo);
$listar->execute();
$dados = $listar->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($dados); 
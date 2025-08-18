<?php

require_once '../config/conector.php';

$dados_buscar = file_get_contents("php://input");
$dados_log = json_decode($dados_buscar, true);

$telefone = $dados_log['telefone'];

$listar = $pdo->prepare('SELECT `pyt_id`,`pyt_nome`, `pyt_telefone`, `pyt_email`, `pyt_nascimento`, `pyt_observacoes` 
                        FROM tb_python_api WHERE $pyt_telefone = :telefone');
$listar->bindParam(':telefone', $telefone);
$listar->execute();
$dados = $listar->fetchAll(PDO::FETCH_ASSOC);
echo json_encode($dados);
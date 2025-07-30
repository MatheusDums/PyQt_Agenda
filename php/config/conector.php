<?php

$pdo = new PDO('mysql:host=localhost;dbname=db_pyt_api', 'root', '');

$stmt = $pdo->prepare('SELECT pyt_id, pyt_nome, pyt_telefone, pyt_email, pyt_nascimento, pyt_observacoes
                         FROM tb_python_api');
$stmt->execute();
$dados = $stmt->fetchAll(PDO::FETCH_ASSOC);

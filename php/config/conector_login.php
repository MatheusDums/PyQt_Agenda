<?php

$pdo = new PDO('mysql:host=localhost;dbname=db_pyt_api', 'root', '');

$stmt = $pdo->prepare('SELECT pyt_id, pyt_user, pyt_senha FROM tb_python_login');
$stmt->execute();
$dados = $stmt->fetchAll(PDO::FETCH_ASSOC);
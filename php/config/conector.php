<?php

$arquivo_ini = '../../config.ini';

if (file_exists($arquivo_ini)) {
  $config = parse_ini_file($arquivo_ini, true);

  if ($config) {
    $userinfo = $config["API"];
    $userPort = $userinfo['port'];
  } else {
    echo "Erro ao analisar arquivo INI.";
  }
} else {
  echo "Arquivo INI não encontrado.";
}

$pdo = new PDO('mysql:host=localhost;port=' . $userPort . ';dbname=db_pyt_api', 'root', '');

$stmt = $pdo->prepare('SELECT pyt_id, pyt_nome, pyt_telefone, pyt_email, pyt_nascimento, pyt_observacoes
                         FROM tb_python_api');
$stmt->execute();
$dados = $stmt->fetchAll(PDO::FETCH_ASSOC);
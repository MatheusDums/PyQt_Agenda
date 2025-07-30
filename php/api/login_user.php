<?php

require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector.php';

$headers = getallheaders();
if(!isset($_SERVER['PHP_AUTH_USER'])){
    header('WWW-Authenticate: Basic realm="API"');
}

$user = $_SERVER['PHP_AUTH_USER'];
$pass = $_SERVER['PHP_AUTH_PW'];
$authorizationHeader = $headers['Authorization'] ?? null;

$payload = json_encode([
    'Id' => $dados['api_id'],
    'exp' => time() + 3600
]);
$token = base64_encode($payload);

if (($dados['api_email'] === $user) and ($dados['api_senha'] === $pass) ) {
    $atualiza = $pdo->prepare("UPDATE tb_api_login SET api_token = :token WHERE api_email = :user");
    $atualiza->bindParam(':token', $token);
    $atualiza->bindParam(':user', $user);
    $atualiza->execute();
    $dadosForm = [
        "Email" => $dados['api_email'],
        "Senha" => $dados['api_senha'],
        "Token" => $token
    ];
    echo Response::json(200, 'Autorizado', $dadosForm);
} else {
    header('WWW-Authenticate: Basic realm="My Realm"');
    header('HTTP/1.0 401 Unauthorized');
    echo Response::json(401, 'Não Autorizado', "");
    die();
}

?>
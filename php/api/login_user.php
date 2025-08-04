<?php

require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector_login.php';

$headers = getallheaders();
if(!isset($_SERVER['PHP_AUTH_USER'])){
    header('WWW-Authenticate: Basic realm="API"');
}

echo $dados_login[0]['pyt_user'];

$user = $_SERVER['PHP_AUTH_USER'];
$pass = $_SERVER['PHP_AUTH_PW'];
$authorizationHeader = $headers['Authorization'] ?? null;

$payload = json_encode([
    'Id' => $dados_login[0]['pyt_id'],
    'exp' => time() + 3600
]);
$token = base64_encode($payload);

if (($dados_login[0]['pyt_user'] === $user) and ($dados_login[0]['pyt_senha'] === $pass) ) {
    $atualiza = $pdo->prepare("UPDATE tb_python_login SET pyt_token = :token WHERE pyt_user = :user");
    $atualiza->bindParam(':token', $token);
    $atualiza->bindParam(':user', $user);
    $atualiza->execute();
    $dadosForm = [
        "Email" => $dados_login[0]['pyt_user'],
        "Senha" => $dados_login[0]['pyt_senha'],
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
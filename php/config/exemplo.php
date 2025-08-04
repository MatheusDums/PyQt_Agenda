<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/dados.php';
require_once '../config/conector.php';


$headers = getallheaders();
$authorizationHeader = $headers['Authorization'] ?? null;
$token = $authorizationHeader;

if(!isset($token)){
    header('WWW-Authenticate: Basic realm="API"');
} else {
    if($token !== $dados['api_token']) {
        header('WWW-Authenticate: Basic realm="API"');
        echo Response::json(401, 'Não Autorizado', "");
    } else {
        
    $dados = file_get_contents("php://input");

    if($dados) {
    $dados_log = json_decode($dados, true);

    $email = $dados_log['email'];
    $senha = $dados_log['senha'];


    $encontrado = false;

    foreach($data as $dataint) {
        if(in_array($email, $dataint) and in_array($senha, $dataint) ) {
            echo Response::json(200, 'success', $dataint);
            $encontrado = true;
            break;
        }
    }

    if($encontrado === false) {
        echo Response::json(400, 'error', 'Credenciais Incorretas');
    }
}
}

    }
?>
<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/dados.php';
require_once '../config/conector.php';
      
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
?>
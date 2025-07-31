<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/dados.php';
require_once '../config/conector_login.php';
      
$dados = file_get_contents("php://input");

    if($dados) {
        $dados_log = json_decode($dados, true);

    if($dados_log) {
        $user = $dados_log['user'];
        $senha = $dados_log['password'];
    
        $encontrado = false;
        
        /* tentar lcoalizar no banco de dados */



        /* 
        foreach($data as $dataint) {
            if(in_array($email, $dataint) and in_array($senha, $dataint) ) {
                echo Response::json(200, 'success', $dataint);
                $encontrado = true;
                break;
            }
        }

        if($encontrado === false) {
            echo Response::json(400, 'error', 'Credenciais Incorretas');
        } */
    }else {
        echo "Erro ao decodificar JSON.";
    }
} else {
    echo "Nenhum dado recebido.";
}
?>
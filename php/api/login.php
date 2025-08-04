<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector_login.php';
      
$dados = file_get_contents("php://input");

    if($dados) {
        $dados_log = json_decode($dados, true);

    if($dados_log) {
        $user = $dados_log['user'];
        $senha = $dados_log['password'];
    
        $encontrado = false;

        $stmt = $pdo->prepare('SELECT pyt_id, pyt_user, pyt_senha FROM tb_python_login');
        $stmt->execute();
        $dados = $stmt->fetchAll(PDO::FETCH_ASSOC);

        foreach($dados as $dataint) {
            if($dataint['pyt_user'] === $user && $dataint['pyt_senha'] === $senha) {
                $encontrado = true;
                echo Response::json(200, 'Autorizado', 'Funcionou');
                break;
            }
        }

        if($encontrado === false) {
            echo Response::json(400, 'error', 'Credenciais Incorretas');
            die();
        } 
    }else {
        echo Response::json(400, 'error', 'Erro ao decodificar JSON');
        die();
    }
} else {
    echo Response::json(400, 'error', 'Nenhum dado recebido');
    die();
}
?>
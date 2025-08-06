<?php
session_start();
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

            $payload = json_encode([
                'Id' => $dados_login[0]['pyt_id'],
                'exp' => time() + 3600
            ]);
            $token = base64_encode($payload);
            $_SESSION['token'] = $token;
            header("Authorization: Bearer " . $token);
            /* $token = md5(uniqid(mt_rand(), true)); */

            if($token) {
                $atualiza = $pdo->prepare("UPDATE tb_python_login SET pyt_token = :token WHERE pyt_user = :user");
                $atualiza->bindParam(':token', $token);
                $atualiza->bindParam(':user', $dataint['pyt_user']);
                $atualiza->execute();
                $dadosForm = [
                    "Email" => $dados_login[0]['pyt_user'],
                    "Senha" => $dados_login[0]['pyt_senha'],
                    "Token" => $token
                ];
            }

            echo Response::json(200, 'Autorizado', ['dados_rec' => $dadosForm]);
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
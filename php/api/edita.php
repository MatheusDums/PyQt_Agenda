<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector.php';

$dados_atualiza = file_get_contents("php://input");

if ($dados_atualiza) {
    $dados_log = json_decode($dados_atualiza, true);

    if ($dados_log) {
        $new_id = $dados_log['id'];
        $new_nome = $dados_log['nome'];
        $new_telefone = $dados_log['telefone'];
        $new_email = $dados_log['email'];
        $new_nascimento = $dados_log['nascimento'];
        $new_observacoes = $dados_log['observacoes'];

        $atualiza = $pdo->prepare("UPDATE tb_python_api SET pyt_nome = :nome,  pyt_telefone = :telefone, pyt_email = :email, 
        pyt_nascimento = :nascimento, pyt_observacoes = :observacoes WHERE pyt_id = :id");

        $atualiza->bindParam(':id', $new_id);
        $atualiza->bindParam(':nome', $new_nome);
        $atualiza->bindParam(':telefone', $new_telefone);
        $atualiza->bindParam(':email', $new_email);
        $atualiza->bindParam(':nascimento', $new_nascimento);
        $atualiza->bindParam(':observacoes', $new_observacoes);

        $atualiza->execute();
        echo Response::json(200, 'Autorizado', 'Ok');

    } else {
        echo "Erro ao decodificar JSON.";
    }
} else {
    echo "Nenhum dado recebido.";
}
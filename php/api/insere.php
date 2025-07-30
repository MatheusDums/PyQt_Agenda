<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/conector.php';

$dados = file_get_contents("php://input");

if ($dados) {
    $dados_log = json_decode($dados, true);

    if ($dados_log) {
/*         $id = $dados_log['id']; */
        $nome = $dados_log['nome'];
        $telefone = $dados_log['telefone'];
        $email = $dados_log['email'];
        $nascimento = $dados_log['nascimento'];
        $observacoes = $dados_log['observacoes'];
        
        $adiciona = $pdo->prepare("INSERT INTO `tb_python_api`(`pyt_id`,`pyt_nome`, `pyt_telefone`, `pyt_email`, `pyt_nascimento`, `pyt_observacoes`) 
        VALUES (:id, :nome, :telefone, :email, :nascimento, :observacoes)");
        $adiciona->bindParam(':id', $id);
        $adiciona->bindParam(':nome', $nome);
        $adiciona->bindParam(':telefone', $telefone);
        $adiciona->bindParam(':email', $email);
        $adiciona->bindParam(':nascimento', $nascimento);
        $adiciona->bindParam(':observacoes', $observacoes);

        $adiciona->execute();

    } else {
        echo "Erro ao decodificar JSON.";
    }
} else {
    echo "Nenhum dado recebido.";
}
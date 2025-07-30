<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/dados.php';
require_once '../config/conector.php';

$dados = file_get_contents("php://input");

if ($dados) {
    $dados_log = json_decode($dados, true);

    if ($dados_log) {
        $id = intval($dados_log['id']);
        echo intval($id);

        $remove = $pdo->prepare("DELETE FROM tb_python_api WHERE pyt_id = :linha");
        $remove->bindParam(':linha', $id);
        $remove->execute();
    } else {
        echo "nenhum dado processado";
    }

} else {
    echo "nenhum dado recebido";
}
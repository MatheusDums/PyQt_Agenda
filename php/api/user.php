<?php
require_once '../config/index.php';
require_once '../config/resposta.php';
require_once '../config/dados.php';
require_once '../config/conector.php';

if(isset($_GET['id'])) {
    $id = $_GET['id'];
    if($id < 0 || $id > count($data) -1 ) {
    echo Response::json(400, 'error', 'Id não encontrado');
    exit;
} else {
    echo Response::json(200, 'success', $data[$id]);
}
} else {
    $dados = file_get_contents("php://input");

    $dados_log = json_decode($dados, true);
    $new_id = $dados_log['id'];

    $newData = [
        "id" => $dados_log['id'],
        "nome" => $dados_log['nome'],
        "idade" => $dados_log['idade'],
        "email" => $dados_log['email'],
        "senha" => $dados_log['senha'],
    ];

    if(isset($data[$new_id])) {
        $data[$new_id] = $newData;
        file_put_contents('../config/dados.php', '<?php $data = ' .  var_export($data, true) . ';');
        echo Response::json(200, 'Dados alterados com succeso:', $data[$new_id]);
    }

}

?>


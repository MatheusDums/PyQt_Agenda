<?php 

class Response
{
    public static function json($status = 200, $message = 'Sucesso', $data = null)
    {
        header('Content-Type: application/json');

        if(!API_IS_ACTIVE) {
            return json_encode([
                'status' => 400,
                'message' => 'A API não está rodando',
                'data' => null
        ], JSON_PRETTY_PRINT);
        }


        return json_encode([
            'status' => $status,
            'message' => $message,
            'data' => $data
        ], JSON_PRETTY_PRINT);
    }
}


?>
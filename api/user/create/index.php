<?php
require_once("../../../includes/main.php");
$session = UserSession();
if(isset($_GET['username'],$_GET['password'])){
    $session = SignupUserSession($session,$_GET['username'],$_GET['password']);
}
$data = ['session'=>CleanSessionData($session)];
OutputJson($data);
?>
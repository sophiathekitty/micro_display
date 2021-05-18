<?php
require_once("../../../includes/main.php");
$session = UserSession();
$session = LogoutUserSession($session['id']);
ClearToken();
$data = ['session'=>CleanSessionData($session)];
OutputJson($data);
?>
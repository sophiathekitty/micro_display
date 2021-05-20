<?php
require_once("../../includes/main.php");
$data = ['session'=>UserSession::CleanSessionData(new UserSession())];
OutputJson($data);
?>
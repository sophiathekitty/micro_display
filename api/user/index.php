<?php
require_once("../../includes/main.php");
$data = ['session'=>CleanSessionData(UserSession())];
OutputJson($data);
?>
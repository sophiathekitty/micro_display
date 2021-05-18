<?php
require_once("../../../includes/main.php");
$data = [];
if(isset($_GET['shutdown'])){
	if($_GET['shutdown']){
			SaveSettingVar('shutdown_requested',1);
	} else {
			SaveSettingVar('shutdown_requested',0);
	}
}
$data['shutdown'] = LoadSettingVar('shutdown_requested');
OutputJson($data);
?>
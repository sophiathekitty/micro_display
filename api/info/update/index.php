<?php
require_once("../../../includes/main.php");
$data = [];
if(isset($_GET['update'])){
	if($_GET['update']){
			SaveSettingVar('check_for_update',1);
	} else {
			SaveSettingVar('check_for_update',0);
	}
}
$data['update'] = LoadSettingVar('check_for_update');
OutputJson($data);
?>
<?php
require_once("../../../includes/main.php");
$data = [];
if(isset($_GET['reboot'])){
	if($_GET['reboot']){
			SaveSettingVar('reboot_requested',1);
	} else {
			SaveSettingVar('reboot_requested',0);
	}
}
$data['reboot'] = LoadSettingVar('reboot_requested');
OutputJson($data);
?>
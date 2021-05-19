<?php
require_once("../../../includes/main.php");
$data = [
	'info' => [
		'url' => $_SERVER['HTTP_HOST'],
		'path' => "http://".$_SERVER['HTTP_HOST'].LoadSettingVar('path'),
		'app_path' => "http://".$_SERVER['HTTP_HOST'].LoadSettingVar('path')."/app",
		'type' => LoadSettingVar('type'),
		'main' => LoadSettingVar('main'),
		'room' => LoadSettingVar('room_id'),
		'enabled' => LoadSettingVar('enabled'),
		'mac_address' => LocalMacAddress(),
		'name' => LoadSettingVar('name')
		]
	];
$data['apis'] = LocalAPIs();
OutputJson($data);
?>
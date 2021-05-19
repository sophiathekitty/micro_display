<?php
require_once("../../includes/main.php");
$data = [
	'info' => [
		'url' => $_SERVER['HTTP_HOST'],
		'room' => LoadSettingVar('room_id'),
		'type' => LoadSettingVar('type'),
		'enabled' => LoadSettingVar('enabled'),
		'main' => LoadSettingVar('main'),
		'path' => LoadSettingVar('path'),
		'server' => LoadSettingVar('server'),
		'mac_address' => LocalMacAddress(),
		'name' => LoadSettingVar('name')
		]
	];
OutputJson($data);
?>

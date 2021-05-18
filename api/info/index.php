<?php
require_once("../../includes/main.php");
$data = [
	'info' => [
		'url' => $_SERVER['HTTP_HOST'],
		'path' => "/extensions"."/".LoadSettingVar('extension_path'),
		'type' => LoadSettingVar('extension_type'),
		'enabled' => LoadSettingVar('extension_enabled'),
		'mac_address' => LocalMacAddress(),
		'name' => LoadSettingVar('extension_name')
		]
	];
OutputJson($data);
?>

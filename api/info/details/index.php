<?php
require_once("../../../includes/main.php");
$data = [
	'info' => [
		'url' => $_SERVER['HTTP_HOST'],
		'path' => "http://".$_SERVER['HTTP_HOST']."/extensions"."/".LoadSettingVar('extension_path'),
		'app_path' => "http://".$_SERVER['HTTP_HOST']."/extensions"."/".LoadSettingVar('extension_path')."/app",
		'type' => LoadSettingVar('extension_type'),
		'enabled' => LoadSettingVar('extension_enabled'),
		'mac_address' => LocalMacAddress(),
		'name' => LoadSettingVar('extension_name')
		]
	];
$data['apis'] = LocalAPIs();
OutputJson($data);
?>
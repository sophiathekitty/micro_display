<?php
require_once("../../../includes/main.php");
$data = [];
if (isset($_GET['name'],$_GET['type'],$_GET['mac_address'],$_GET['url'])){
	$server = ServerMacAddress($_GET['mac_address']);
	if(is_null($server)){
		$data['added'] = AddServer($_GET['name'],$_GET['type'],$_GET['mac_address'],$_GET['url']);
	} else {
		$data['updated'] = UpdateServer($_GET['name'],$_GET['type'],$_GET['mac_address'],$_GET['url']);
	}
}
// return servers
if(isset($_GET['online'])){
	$data['servers'] = OnlineServers();
} elseif(isset($_GET['offline'])){
	$data['servers'] = OfflineServers();
} else {
	$data['servers'] = AllServers();
}
OutputJson($data);
?>
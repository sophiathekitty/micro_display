<?php
function AllServers(){
    return clsDB::$db_g->select("SELECT * FROM `servers`");
}
function OnlineServers(){
    return clsDB::$db_g->select("SELECT * FROM `servers` WHERE `online` = '1'");
}
function OfflineServers(){
    return clsDB::$db_g->select("SELECT * FROM `servers` WHERE `online` = '0'");
}
function ServerIP($ip){
    if(strpos($ip,"::1") > -1 || $ip == "localhost"){
        return ['id'=>0,'name'=>'localhost','url'=>$ip,'mac_address'=>"localhost"];
    }
    $server = clsDB::$db_g->select("SELECT * FROM `servers` WHERE `url` = '$ip'");
    if(count($server)){
        return $server[0];
    }
    return NULL;
}
function ServerMacAddress($mac_address){
    $server = clsDB::$db_g->select("SELECT * FROM `servers` WHERE `mac_address` = '$mac_address' ORDER BY `last_ping` DESC");
    if(count($server)){
        return $server[0];
    }
    return NULL;
}
function PingServer($mac_address){
    $time = date("Y-m-d H:i:s");
    clsDB::$db_g->safe_update('servers',['last_ping'=>$time],['mac_address'=>$mac_address]);
}
function AddServer($name,$type,$mac_address,$url){
    clsDB::$db_g->safe_inserts('servers',array(
        "name" => $name,
        "mac_address" => $mac_address,
        "type" => $type,
        "url" => $url,
        "last_ping" =>  date("Y-m-d H:i:s",time()),
        "online" => 1
    ));
    return ServerMacAddress($mac_address);
}
function UpdateServer($name,$type,$mac_address,$url){
    clsDB::$db_g->safe_update('servers',array(
        "name" => $name,
        "type" => $type,
        "url" => $url,
        "last_ping" =>  date("Y-m-d H:i:s",time()),
        "online" => 1
    ), array(
        "mac_address" => $mac_address
    ));
    return ServerMacAddress($mac_address);
}
?>
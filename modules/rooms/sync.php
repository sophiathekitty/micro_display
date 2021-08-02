<?php
function SyncRooms(){
    echo "SyncRooms?\n";
    if(Settings::LoadSettingsVar('main',0)) return null;
    echo "Not hub...\n";
    $hub = Servers::GetHub();
    if(is_null($hub)) return null;
    echo "hub found...\n";
    $url = "http://".$hub['url']."/api/rooms/";
    echo "url: $url \n";
    //$url = "http://".$hub['url']."/api/rooms/?simple=1";
    //$url = "http://".$hub['url']."/api/rooms/?room_id=".Settings::LoadSettingsVar('room_id');
    return SyncRoomUrl($url);
}
function SyncRoom(){
    if(Settings::LoadSettingsVar('main',0)) return null;
    $hub = Servers::GetHub();
    if(is_null($hub)) return null;
    $url = "http://".$hub['url']."/api/rooms/?room_id=".Settings::LoadSettingsVar('room_id');
    return SyncRoomUrl($url);
}
function SyncRoomUrl($url){
    $info = file_get_contents($url);
    $data = json_decode($info,true);
    print_r($data);
    echo "\n";
    if(isset($data['rooms'])){
        foreach($data['rooms'] as $room){
            // save room
            Rooms::SaveRoom($room);
            echo clsDB::$db_g->get_err();
        }    
    }
    if(isset($data['room'])){
        Rooms::SaveRoom(($data['room']));
        echo clsDB::$db_g->get_err();
    }
    return Rooms::AllRooms();
}
?>
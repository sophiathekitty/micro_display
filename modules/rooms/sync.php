<?php
function SyncRooms(){
    if(Settings::LoadSettingsVar('main',0)) return null;
    $hub = Servers::GetHub();
    if(is_null($hub)) return null;
    $url = "http://".$hub['url']."/api/rooms/?simple=1";
    $info = file_get_contents($url);
    $data = json_decode($info,true);
    //print_r($data);
    foreach($data['rooms'] as $room){
        // save room
        Rooms::SaveRoom($room);
        echo clsDB::$db_g->get_err();
    }
    return Rooms::AllRooms();
}
?>
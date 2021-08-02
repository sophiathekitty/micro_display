<?php
require_once("../../includes/main.php");
$data = [];
if($_GET['room_id']){
    $data['room'] = Rooms::RoomId($_GET['room_id']);
} else {
    $data['rooms'] = Rooms::AllRooms();
}
OutputJson($data);
?>

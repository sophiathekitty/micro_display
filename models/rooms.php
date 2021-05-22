<?php
class Rooms extends clsModel{
    public $table_name = "Rooms";
    public $fields = [
        [
            'Field'=>"id",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"PRI",
            'Default'=>"",
            'Extra'=>"auto_increment"
        ],[
            'Field'=>"name",
            'Type'=>"varchar(100)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"",
            'Extra'=>""
        ],[
            'Field'=>"floor",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"1",
            'Extra'=>""
        ],[
            'Field'=>"bedtime",
            'Type'=>"time",
            'Null'=>"YES",
            'Key'=>"",
            'Default'=>null,
            'Extra'=>""
        ],[
            'Field'=>"awake_time",
            'Type'=>"time",
            'Null'=>"YES",
            'Key'=>"",
            'Default'=>null,
            'Extra'=>""
        ],[
            'Field'=>"activity",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"0",
            'Extra'=>""
        ],[
            'Field'=>"sunlight_offset",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"2",
            'Extra'=>""
        ],[
            'Field'=>"hide_room",
            'Type'=>"tinyint(1)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"0",
            'Extra'=>""
        ]
    ];


    private static $rooms = null;
    private static function GetInstance(){
        if(is_null(Rooms::$rooms)) Rooms::$rooms = new Rooms();
        return Rooms::$rooms;
    }
    public static function SaveRoom($data){
        $rooms = Rooms::GetInstance();
        $room = $rooms->LoadById($data['id']);
        if(is_null($room)){
            $rooms->Save($data);
        } else {
            $rooms->Save($data,['id'=>$data['id']]);
        }
    }
    public static function AllRooms(){
        $rooms = Rooms::GetInstance();
        return $rooms->LoadAll();
    }
    public static function RoomId($id){
        $rooms = Rooms::GetInstance();
        return $rooms->LoadById($id);
    }
    public static function RoomName($name){
        $rooms = Rooms::GetInstance();
        return $rooms->LoadWhere(['name'=>$name]);
    }
}
if(defined('VALIDATE_TABLES')){
    clsModel::$models[] = new Rooms();
}
?>
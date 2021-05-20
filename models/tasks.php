<?php

class Tasks extends clsModel {
    public $table_name = "Tasks";
    public $fields = [
        [
            'Field'=>"id",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"PRI",
            'Default'=>"",
            'Extra'=>"auto_increment"
        ],[
            'Field'=>"room_id",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"",
            'Extra'=>""
        ],[
            'Field'=>"assigned_to",
            'Type'=>"int(11)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"",
            'Extra'=>""
        ],[
            'Field'=>"completed_by",
            'Type'=>"int(11)",
            'Null'=>"YES",
            'Key'=>"",
            'Default'=>null,
            'Extra'=>""
        ],[
            'Field'=>"name",
            'Type'=>"varchar(50)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"",
            'Extra'=>""
        ],[
            'Field'=>"skipped",
            'Type'=>"tinyint(1)",
            'Null'=>"YES",
            'Key'=>"",
            'Default'=>null,
            'Extra'=>""
        ],[
            'Field'=>"created",
            'Type'=>"datetime",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"current_timestamp()",
            'Extra'=>""
        ],[
            'Field'=>"due",
            'Type'=>"datetime",
            'Null'=>"YES",
            'Key'=>"",
            'Default'=>null,
            'Extra'=>""
        ],[
            'Field'=>"completed",
            'Type'=>"datetime",
            'Null'=>"YES",
            'Key'=>"",
            'Default'=>null,
            'Extra'=>""
        ]
    ];
}


if(defined('VALIDATE_TABLES')){
    clsModel::$models[] = new Tasks();
}

/*

function LoadAllTasks(){
    return clsDB::$db_g->select("SELECT * FROM `Task`;");
}
function LoadActiveTasks(){
    return clsDB::$db_g->select("SELECT * FROM `Task` WHERE `completed` IS NULL;");
}
function LoadTask($id){
    $row = clsDB::$db_g->select("SELECT * FROM `Task` WHERE `id` = '$id';");
    if(count($row) > 0){
        return $row[0];
    }
    return null;
}
function LoadTaskNameToday($name){
    return LoadTaskNameDay($name,date("Y-m-d"));
}
function LoadTaskNameDay($name,$day){
    $tomorrow = date("Y-m-d",strtotime($day));
    $row = clsDB::$db_g->select("SELECT * FROM `Task` WHERE `name` = '$name' AND DATE(`created`) BETWEEN '$day' AND '$tomorrow';");
    if(count($row) > 0){
        return $row[0];
    }
    return null;
}
function LoadAllTasksRoom($room_id){
    return clsDB::$db_g->select("SELECT * FROM `Task` WHERE `room_id` = '$room_id' OR `room_id` = '0';");
}
function LoadActiveTasksRoom($room_id){
    return clsDB::$db_g->select("SELECT * FROM `Task` WHERE `completed` IS NULL AND (`room_id` = '$room_id' OR `room_id` = '0');");
}
function CreateTask($room_id,$assigned_to,$name,$due = null){
    $id  = clsDB::$db_g->safe_insert('Task',['room_id'=>$room_id,'assigned_to'=>$assigned_to,'name'=>$name,'due'=>$due]);
//    echo clsDB::$db_g->get_err()."<br>";
    return LoadTask($id);
}
function UpdateTask($id,$update){
    clsDB::$db_g->safe_update('Task',$update,['id'=>$id]);
    return LoadTask($id);
}
function PruneTasks($d){

}
*/
?>
<?php
function LoadColors(){
    return clsDB::$db_g->select("SELECT * FROM `Colors`");
}
function LoadColor($id){
    $row = clsDB::$db_g->select("SELECT * FROM `Colors` WHERE `id` = '$id' LIMIT 1;");
    if(count($row)){
        return $row[0]['color'];
    }
    return null;
}
function SaveColor($id,$color){
    $c = LoadColor($id);
    if(is_null($c)){
        // insert
        clsDB::$db_g->safe_insert("Colors",['id'=>$id,'color'=>$color]);
    } else {
        // update
        clsDB::$db_g->safe_insert("Colors",['color'=>$color],['id'=>$id]);
    }
    return LoadColor($id);
}
?>
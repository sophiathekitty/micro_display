<?php
/*
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
*/
class Colors extends clsModel {
    public $table_name = "Colors";
    public $fields = [
        [
            'Field'=>"id",
            'Type'=>"varchar(20)",
            'Null'=>"NO",
            'Key'=>"PRI",
            'Default'=>"",
            'Extra'=>""
        ],[
            'Field'=>"color",
            'Type'=>"varchar(7)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"",
            'Extra'=>""
        ],[
            'Field'=>"pallet",
            'Type'=>"varchar(10)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"general",
            'Extra'=>""
        ]
    ];

    public function SaveColor($id,$color,$pallet = "general"){
        return $this->Save(['id'=>$id,'color'=>$color,'pallet'=>$color],['id'=>$id]);
    }
    public function LoadColor($id){
        return $this->LoadById($id);
    }
    public function LoadPallet($pallet){
        return $this->LoadAllWhere(['pallet'=>$pallet]);
    }
    public function PalletsList(){
        $rows = clsDB::$db_g->select("SELECT DISTINCT `pallet` FROM `".$this->table_name."`");
        $pallets = [];
        foreach($rows as $row){
            $pallets[] = $row['pallet'];
        }
        return $pallets;
    }
}
if(defined('VALIDATE_TABLES')){
    clsModel::$models[] = new Colors();
}
?>
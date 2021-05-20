<?php
/* 
ok... so if  i'm going to bother having a model class it should solve some basic problems

1. be able to install it's table
2. be able to validate and update it's table

and it should be able to lint nicely... so probably do everything as static functions
*/


class clsModel {
    public static $models = [];
    public static function ValidateTables(){
        foreach(clsModel::$models as $model){
            $model->ValidateTable();
        }
    }
    public function ValidateTable(){
        if(!clsDB::$db_g->has_table($this->table_name)){
            clsDB::$db_g->install_table($this->table_name,$this->fields);
        }
        $table = clsDB::$db_g->describe_table($this->table_name);
        //print_r($table);
        $after = "";
        // check for missing or changed fields
        foreach($this->fields as $field){
            $has = $this->TableHasField($table,$field);
            switch($has){
                case "Missing":
                    // add the field
                    clsDB::$db_g->add_field($this->table_name,$field,$after);
                    break;
                case "Changed":
                    // add the field
                    //echo "Field changed: ".$field['Field']."\n";
                    clsDB::$db_g->update_field($this->table_name,$field);
                    //echo clsDB::$db_g->get_err();
                    break;
            }
            $after = $field['Field'];
        }
        // check for fields that have been removed
        foreach($table as $field){
            if($this->TableHasDepreciatedField($field)){
                clsDB::$db_g->remove_field($this->table_name,$field);
            }
        }
    }
    private function TableHasField($table,$field){
        foreach($table as $f){
            if($f['Field'] == $field['Field']){
                if($f['Type'] != $field['Type']) return "Changed";
                if($f['Null'] != $field['Null']) return "Changed";
                if($f['Key'] != $field['Key']) return "Changed";
                if($f['Default'] != $field['Default']) return "Changed";
                if($f['Extra'] != $field['Extra']) return "Changed";
                return "Found";
            }
        }
        return "Missing";
    }
    private function TableHasDepreciatedField($field){
        foreach($this->fields as $f){
            if($field['Field'] == $f['Field']) return false;
        }
        return true;
    }

    public function LoadAll(){
        return clsDB::$db_g->safe_select($this->table_name);
    }

    public function LoadById($id){
        $rows = clsDB::$db_g->safe_select($this->table_name,['id'=>$id]);
        if(count($rows) > 0) return $rows[0];
        return null;
    }
    public function LoadWhere($where){
        $rows = clsDB::$db_g->safe_select($this->table_name,$where);
        if(count($rows) > 0) return $rows[0];
        return null;
    }
    public function LoadAllWhere($where){
        return clsDB::$db_g->safe_select($this->table_name,$where);
    }

    public function Save($data,$where = null){
        // check for matching record
        $id = null;
        $row = null;
        if($where){
            $row = $this->LoadWhere($where);
        }
        if(is_null($row)){
            // record doesn't exist insert a new one
            $id = clsDB::$db_g->safe_insert($this->table_name,$data,$where);
        } else {
            // record already exists so update it
            $id = clsDB::$db_g->safe_update($this->table_name,$data,$where);
            $row = $this->LoadWhere($where);
        }
        return ['last_insert_id'=>$id,'error'=>clsDB::$db_g->get_err(),'row'=>$row];
    }

    // this needs to be overwritten by the individual models
    public $table_name = "Example";
    public $fields = [
        [
            "Field"=>"id",
            "Type"=>"int(11)",
            "Null"=>"NO",
            "Key"=>"PRI",
            "Default"=>"",
            "Extra"=>"auto_increment"
        ]
    ];
}
?>
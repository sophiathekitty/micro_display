<?php
/* 
ok... so if  i'm going to bother having a model class it should solve some basic problems

1. be able to install it's table
2. be able to validate and update it's table

and it should be able to lint nicely... so probably do everything as static functions
*/


class clsModel {
    public function ValidateTable(){
        if(!clsDB::$db_g->has_table($this->table_name)){
            clsDB::$db_g->install_table($this->table_name,$this->fields);
        }
        $table = clsDB::$db_g->describe_table($this->table_name);
        print_r($table);
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
                    echo "Field changed: ".$field['Field']."\n";
                    clsDB::$db_g->update_field($this->table_name,$field);
                    echo clsDB::$db_g->get_err();
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


    // this needs to be overwritten by the individual models
    public $table_name = "Example";
    public $fields = [
        [
            "Field"=>"id",
            "Type"=>"id",
            "Null"=>"id",
            "Key"=>"",
            "Default"=>"",
            "Extra"=>""
        ]
    ];
}
?>
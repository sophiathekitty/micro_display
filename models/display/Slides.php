<?php
class SlideSections extends clsModel{
    public $table_name = "SlideSections";
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
            'Type'=>"varchar(20)",
            'Null'=>"NO",
            'Key'=>"",
            'Default'=>"",
            'Extra'=>""
        ]
    ];


    private static $slides = null;
    private static function GetInstance(){
        if(is_null(SlideSections::$slides)) SlideSections::$slides = new SlideSections();
        return SlideSections::$slides;
    }
    public static function GetSections(){
        $slides = SlideSections::GetInstance();
        return $slides->LoadAll();
    }
}
if(defined('VALIDATE_TABLES')){
    clsModel::$models[] = new SlideSections();
}
?>
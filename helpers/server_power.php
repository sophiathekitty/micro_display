<?php
require_once("../includes/main.php");
$check_for_update = LoadSettingVar("check_for_update");
if(!is_null($check_for_update) && (int)$check_for_update == 1){
    UpdateFromGit();
}

// testing... should probably remove if it all works
UpdateFromGit();

?>
<?php
function LocalPluginApis($apis){
    global $root_path;
    $plugins = FindPluginsLocal($root_path."plugins/");
    foreach($plugins as $plugin){
        $apis = APIFolder($root_path,"plugins/".$plugin."api/",$apis);
    }
    return $apis;
}
?>
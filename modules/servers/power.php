<?php
function ShutdownDevice(){
    SaveSettingVar('shutdown_requested',0);
    shell_exec("sudo shutdown now");
}
function RebootDevice(){
    SaveSettingVar('reboot_requested',0);
    shell_exec("sudo shutdown -r now");
}
function UpdateFromGit(){
    SaveSettingVar("check_for_update",0);
    echo shell_exec("git pull");
}
?>
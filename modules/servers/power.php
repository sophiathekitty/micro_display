<?php
function ShutdownDevice(){
    SaveSettingVar('shutdown_requested',0);
    shell_exec("sudo shutdown +1");
}
function RebootDevice(){
    SaveSettingVar('reboot_requested',0);
    shell_exec("sudo shutdown -r +1");
}
function UpdateFromGit(){
    SaveSettingVar("check_for_update",0);
    echo "we're doing the shell script maybe?\n";
    echo shell_exec("sh /var/www/html/gitpull.sh");
}
?>
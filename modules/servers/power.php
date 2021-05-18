<?php
function ShutdownDevice(){
    shell_exec("sudo shutdown now");
}
function RebootDevice(){
    shell_exec("sudo shutdown -r now");
}
?>
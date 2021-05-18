<?php
require_once("../../includes/main.php");
$data = [];

if(isset($_GET['pallet'])){
    $data['pallet'] = FullColorPallet();
} else {
    $data['colors'] = LoadColors();
}

OutputJson($data);
?>
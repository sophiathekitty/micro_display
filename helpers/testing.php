<pre><?php
require_once("../includes/main.php");

//$testing = new TestingModel();
//$testing->ValidateTable();

$colors = new Colors();
$colors->ValidateTable();
$pallets = $colors->PalletsList();
print_r($pallets);
$color = $colors->LoadColor('am');
print_r($color);
print_r($colors->LoadAll());
?></pre>
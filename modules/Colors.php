<?php
function FullColorPallet(){
    $pallet = [];
    $pallet['display_default'] = LoadColor('display_default');
    $pallet['clock'] = ClockColorPallet();
    $pallet['weather'] = WeatherColorPallet();
    $pallet['stoner'] = StonerColorPallet();
    $pallet['strains'] = StrainsColorPallet();
    return $pallet;
}
function WeatherColorPallet(){
    $pallet = [];
    $pallet['temperature'] = TemperatureColorPallet();
    $pallet['humidity'] = [LoadColor('hum_min'),LoadColor('hum_max')];
    $pallet['wind'] = [LoadColor('wind_min'),LoadColor('wind_max')];
    return $pallet;
}
function TemperatureColorPallet(){
    $pallet=[];
    $pallet[] = LoadColor('temp_0');
    $pallet[] = LoadColor('temp_1');
    $pallet[] = LoadColor('temp_2');
    $pallet[] = LoadColor('temp_3');
    $pallet[] = LoadColor('temp_4');
    $pallet[] = LoadColor('temp_5');
    $pallet[] = LoadColor('temp_6');
    $pallet[] = LoadColor('temp_7');
    $pallet[] = LoadColor('temp_8');
    $pallet[] = LoadColor('temp_9');
    $pallet[] = LoadColor('temp_10');
    $pallet[] = LoadColor('temp_11');
    return $pallet;
}
function StonerColorPallet(){
    return [
        'fourOhFour'=>LoadColor('fourOhFour'),
        'fourTwenty'=>LoadColor('fourTwenty'),
        'sevenTen'=>LoadColor('sevenTen')
    ];
}
function StrainsColorPallet(){
    return [
        'indica'=>LoadColor('indica'),
        'indicaHybrid'=>LoadColor('indicaHybrid'),
        'hybrid'=>LoadColor('hybrid'),
        'sativaHybrid'=>LoadColor('sativaHybrid'),
        'sativa'=>LoadColor('sativa')
    ];
}
function ClockColorPallet(){
    return [
        'am'=>LoadColor('am'),
        'pm'=>LoadColor('pm'),
        'oneTwoThreeFour'=>LoadColor('oneTwoThreeFour'),
        'elevenEleven'=>LoadColor('elevenEleven'),
        'fourFiveSix'=>LoadColor('fourFiveSix'),
        'oneOneOne'=>LoadColor('oneOneOne')
    ];
}
?>
<?php

$x = 10;
$y = 20;

function multic() {

$GLOBALS['z'] =$GLOBALS['x'] + $GLOBALS['y'];

}

multic();
echo $z;
?>
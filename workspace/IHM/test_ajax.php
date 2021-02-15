<?php
header('Content-Type: text/xml;charset=utf-8');
echo(utf8_encode("<?xml version='1.0' encoding='UTF-8' ?><options>"));
if (isset($_GET['debut'])) {
    $debut = utf8_decode($_GET['debut']);
} else {
    $debut = "";
}
$debut = strtolower($debut);
$liste = array([...]);
 
function generateOptions($debut,$liste) {
    $MAX_RETURN = 10;
    $i = 0;
    foreach ($liste as $element) {
        if ($i<$MAX_RETURN && substr($element, 0, strlen($debut))==$debut) {
            echo(utf8_encode("<option>".$element."</option>"));
            $i++;
        }
    }
}
 
generateOptions($debut,$liste);
 
echo("</options>");
?>
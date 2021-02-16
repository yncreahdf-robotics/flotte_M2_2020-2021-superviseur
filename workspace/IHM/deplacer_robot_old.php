<?php

	$Robot = $_POST["Robot"];
	$Position = $_POST["Position"];

	$output = passthru("python CommandeRobot.py $Robot $Position");
	
	echo "Sent message ID: {$mid}\n";

?>


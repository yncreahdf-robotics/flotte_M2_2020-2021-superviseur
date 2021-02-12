<?php

	$Robot = $_POST["Robot"];
	$Position = $_POST["Position"];
	
	$client = new \Mosquitto\Client();
	$client->onConnect('connect');
	$client->onDisconnect('disconnect');
	$client->onSubscribe('subscribe');
	$client->onMessage('message');
	$client->connect("localhost", 1883, 5);
	
	$mid = $client->publish("Service/Arrived/Table", "1" , 2, 0);
	echo "Sent message ID: {$mid}\n";


	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");


?>

<?php
	require 'phpMQTT.php'

	$Robot = $_POST["Robot"];
	$Position = $_POST["Position"];

	try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}


?>
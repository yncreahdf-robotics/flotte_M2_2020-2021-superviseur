<?php
	require 'phpMQTT.php'

	$Robot = $_POST["Robot"];
	$Position = $_POST["Position"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");


?>
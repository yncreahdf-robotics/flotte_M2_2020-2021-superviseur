<?php
	$nom_position = $_POST["nom_position"];
	$position_X = $_POST["position_X"];
	$position_Y = $_POST["position_Y"];
	$position_Z = $_POST["position_Z"];
	$position_W = $_POST["position_W"];

	try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}

	$requete = $bdd->prepare('INSERT INTO Pose_tb(PoseName, PoseX, PoseY, PoseZ, PoseW) VALUES(:nom_position, :position_X, :position_Y, :position_Z, :position_W)');
	$requete->execute(array(
		'nom_position' => $nom_position,
		'position_X' => $position_X,
		'position_Y' => $position_Y,
		'position_Z' => $position_Z,
		'position_W' => $position_W
	));

	header('Location: IHM_Liste_Positions.php');
?>
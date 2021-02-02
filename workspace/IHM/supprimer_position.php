<?php
	$selected_position = $_POST["selected_position"];

	try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}

	$requete = $bdd->prepare('DELETE FROM Pose_tb WHERE PoseID = :selected_position');
	$requete->execute(array(
		'selected_position' => $selected_position
	));

	header('Location: IHM_Liste_Positions.php');
?>
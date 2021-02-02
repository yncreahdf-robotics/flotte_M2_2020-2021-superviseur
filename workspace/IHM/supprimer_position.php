<?php
	$selected_position = $_POST["selected_position"];

	include("connexion.php");

	$requete = $bdd->prepare('DELETE FROM Pose_tb WHERE PoseID = :selected_position');
	$requete->execute(array(
		'selected_position' => $selected_position
	));

	header('Location: IHM_Liste_Positions.php');
?>
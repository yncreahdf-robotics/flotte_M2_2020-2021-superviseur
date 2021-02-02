<?php
	$selected_position = $_POST["selected_position"];
	$new_nom_position = $_POST["new_nom_position"];
	$new_position_X = $_POST["new_position_X"];
	$new_position_Y = $_POST["new_position_Y"];
	$new_position_Z = $_POST["new_position_Z"];
	$new_position_W = $_POST["new_position_W"];

	include("connexion.php");

	$requete = $bdd->prepare('UPDATE Pose_tb SET PoseName = :new_nom_position, PoseX = :new_position_X, PoseY = :new_position_Y, PoseZ = :new_position_Z, PoseW = :new_position_W WHERE PoseID = :selected_position');
	$requete->execute(array(
		'new_nom_position' => $new_nom_position,
		'new_position_X' => $new_position_X,
		'new_position_Y' => $new_position_Y,
		'new_position_Z' => $new_position_Z,
		'new_position_W' => $new_position_W,
		'selected_position' => $selected_position
	));

	header('Location: IHM_Liste_Positions.php');
?>
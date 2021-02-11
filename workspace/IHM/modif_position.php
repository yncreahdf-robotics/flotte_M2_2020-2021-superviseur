<?php

	/*Récupération des données envoyées par le formulaire de modification de boisson*/
	$selected_position = $_POST["selected_position"];
	$new_nom_position = $_POST["new_nom_position"];
	$new_position_X = $_POST["new_position_X"];
	$new_position_Y = $_POST["new_position_Y"];
	$new_position_Z = $_POST["new_position_Z"];
	$new_position_W = $_POST["new_position_W"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va modifier la position dans la table Pose_tb. On modifie la position indiquée par l'ID de la recette récupéré du formulaire et on remplace chaque champ par les informations du formulaire. Le premier champ prend la première variable, le deuxième champ prend la deuxième variable, etc...*/
	$requete = $bdd->prepare('UPDATE Pose_tb SET PoseName = :new_nom_position, PoseX = :new_position_X, PoseY = :new_position_Y, PoseZ = :new_position_Z, PoseW = :new_position_W WHERE PoseID = :selected_position');
	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'new_nom_position' => $new_nom_position,
		'new_position_X' => $new_position_X,
		'new_position_Y' => $new_position_Y,
		'new_position_Z' => $new_position_Z,
		'new_position_W' => $new_position_W,
		'selected_position' => $selected_position
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Positions.php*/
	header('Location: IHM_Liste_Positions.php');
?>
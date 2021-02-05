<?php

	/*Récupération des données envoyées par le formulaire d'ajout de position*/
	$nom_position = $_POST["nom_position"];
	$position_X = $_POST["position_X"];
	$position_Y = $_POST["position_Y"];
	$position_Z = $_POST["position_Z"];
	$position_W = $_POST["position_W"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va ajouter la position dans la table Pose_tb, le premier champ prend la valeur de la première variable, le deuxième champ prend la valeur de la deuxième variable, etc...*/
	$requete = $bdd->prepare('
		INSERT INTO Pose_tb(PoseName, PoseX, PoseY, PoseZ, PoseW) 
		VALUES(:nom_position, :position_X, :position_Y, :position_Z, :position_W)
	');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'nom_position' => $nom_position,
		'position_X' => $position_X,
		'position_Y' => $position_Y,
		'position_Z' => $position_Z,
		'position_W' => $position_W
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Positions.php*/
	header('Location: IHM_Liste_Positions.php');
?>
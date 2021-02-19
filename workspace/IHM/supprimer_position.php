<?php
/*Fonction appelée lorsqu'on veut supprimer une position de la base de données*/

	/*Récupération de l'ID de la position à supprimer depuis le formulaire*/
	$selected_position = $_POST["selected_position"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va supprimer la position dans la table Pose_tb. On supprime la position indiquée par l'ID récupéré du formulaire*/
	$requete = $bdd->prepare('DELETE FROM Pose_tb WHERE PoseID = :selected_position');

	/*On associe la variable de la requète avec la variable récupérée du formulaire*/
	$requete->execute(array(
		'selected_position' => $selected_position
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Positions.php*/
	header('Location: IHM_Liste_Positions.php');
?>
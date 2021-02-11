<?php

	/*Récupération de l'ID de la bouteille à supprimer depuis le formulaire*/
	$bouteille_supprimee = $_POST["bouteille_supprimee"];
	
	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va supprimer la bouteille dans la table Bouteille_tb. On supprime la bouteille indiquée par l'ID récupéré du formulaire*/
	$requete = $bdd->prepare('DELETE FROM Bouteille_tb WHERE BouteilleID = :bouteille_supprimee');

	/*On associe la variable de la requète avec la variable récupérée du formulaire*/
	$requete->execute(array(
		'bouteille_supprimee' => $bouteille_supprimee
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Articles.php*/
	header('Location: IHM_Liste_Articles.php');
?>
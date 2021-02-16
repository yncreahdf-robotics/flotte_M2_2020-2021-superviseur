<?php

	/*On récupère le numéro de la commande à supprimer*/
	$commande_supprimee = $_POST["commande_supprimee"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va supprimer la commande dans la table Commande_tb. On supprime la commande indiquée par le numéro de commande récupéré du formulaire*/
	$requete = $bdd->prepare('
		DELETE FROM Commande_tb 
		WHERE CommandNbr = :commande_supprimee
	');

	/*On associe la variable de la requète avec la variable récupérée du formulaire*/
	$requete->execute(array(
		'commande_supprimee' => $commande_supprimee
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Commandes.php*/
	header('Location: IHM_Liste_Commandes.php');
?>
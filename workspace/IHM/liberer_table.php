<?php
/*Fonction qui permet de libérer une table lorsqu'un client quitte le restaurant et supprime les commandes associsées au client de la abse de données*/

	$liberer_table = $_POST["liberer_table"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va supprimer les commandes associées à la table que l'on libère*/
	$requete_commande = $bdd->prepare('
		DELETE c FROM Commande_tb c
		INNER JOIN Table_tb t
		ON c.CommandNbr = t.CommandNbr
		WHERE t.TableID = :liberer_table
	');
	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete_commande->execute(array(
		'liberer_table' => $liberer_table
	));


	/*Création de la requète qui va réinitialiser la table sélectionnée*/
	$requete = $bdd->prepare('
		UPDATE Table_tb
		SET Etat = \'FREE\', Prix = 0, CommandNbr = 0
		WHERE TableID = :liberer_table	
	');
	/*On associe les variables de la requète avec les variables récuperées du formulaire*/
	$requete->execute(array(
		'liberer_table' => $liberer_table
	));

	/*On renvoit l'utilisateur sur la page IHM_Suivi_Salle.php*/
	header('Location: IHM_Suivi_Salle.php');
?>
<?php

	/*Récupération des données envoyées par le formulaire de modification de boisson*/
	$bouteille_modifiee = $_POST["bouteille_modifiee"];
	$nom_bouteille = $_POST["nom_bouteille"];
	$doseur = $_POST["doseur"];
	$emplacement = $_POST["emplacement"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*On regarde si la bouteille modifiée a été placée sur le tourniquet. Si elle l'a été, on indique dans la bdd qu'on détache la bouteille qui était à la place de la bouteille modifiée avec la requete modif_emplacement qui va mettre à 0 l'emplacement de la bouteille qui était à la place de la bouteille modifiée*/
	if($emplacement != 0){
		$modif_emplacement = $bdd->prepare('
			UPDATE Bouteille_tb 
			SET Emplacement = 0 
			WHERE Emplacement = :emplacement
		');
		$modif_emplacement->execute(array(
			'emplacement' => $emplacement
		));
	}

	/*Création de la requète qui va modifier la boisson dans la table Bouteille_tb. On modifie la boisson indiquée par l'ID de la recette récupéré du formulaire et on remplace chaque champ par les informations du formulaire. Le premier champ prend la première variable, le deuxième champ prend la deuxième variable, etc...*/
	$requete = $bdd->prepare('
		UPDATE Bouteille_tb 
		SET BouteilleName = :nom_bouteille, VolumeDoseur = :doseur, Emplacement = :emplacement 
		WHERE BouteilleID = :bouteille_modifiee
	');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'nom_bouteille' => $nom_bouteille,
		'doseur' => $doseur,
		'emplacement' => $emplacement,
		'bouteille_modifiee' => $bouteille_modifiee
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Articles.php*/
	header('Location: IHM_Liste_Articles.php');
?>
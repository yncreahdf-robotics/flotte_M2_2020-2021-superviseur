<?php
/*Fonction php appelée par le formulaire de déplacement de bouteille de la page IHM_Deplacer_Bouteille.php, elle permet d'ajouter, de déplacer ou d'enlever une bouteille sur le tourniquet*/

	/*Récupération des données envoyées par le formulaire de modification de boisson*/
	$bouteille_modifiee = $_POST["bouteille_modifiee"];
	$emplacement = $_POST["emplacement"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*On regarde si la bouteille déplacée a été placée sur le tourniquet. Si elle l'a été, on indique dans la bdd qu'on détache la bouteille qui était à la place de la bouteille modifiée avec la requete modif_emplacement qui va mettre à 0 l'emplacement de la bouteille qui était à la place de la bouteille modifiée*/
	if($emplacement != 0){
		$modif_emplacement = $bdd->prepare('UPDATE Bouteille_tb SET Emplacement = 0 WHERE Emplacement = :emplacement');
		$modif_emplacement->execute(array(
			'emplacement' => $emplacement
		));
	}

	/*Création de la requète qui va modifier l'emplacement de la bouteille séléectionnée par le formulaire dans la table Bouteille_tb*/
	$requete = $bdd->prepare('
		UPDATE Bouteille_tb 
		SET Emplacement = :emplacement
		WHERE BouteilleID = :bouteille_modifiee
	');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'emplacement' => $emplacement,
		'bouteille_modifiee' => $bouteille_modifiee
	));

	/*On renvoit l'utilisateur sur la page IHM_Suivi_Salle.php*/
	header('Location: IHM_Suivi_Salle.php');
?>
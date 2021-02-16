<?php

	/*Récupération des données envoyées par le formulaire de modification de boisson*/
	$modif_boisson = $_POST["modif_boisson"];
	$nom_boisson = $_POST["nom_boisson"];
	$prix_boisson = $_POST["prix_boisson"];
	$volume_boisson = $_POST["volume_boisson"];
	$liquide1 = $_POST["liquide1"];
	$liquide1_dose = $_POST["liquide1_dose"];
	$liquide2 = $_POST["liquide2"];
	$liquide2_dose = $_POST["liquide2_dose"];
	$liquide3 = $_POST["liquide3"];
	$liquide3_dose = $_POST["liquide3_dose"];
	$liquide4 = $_POST["liquide4"];
	$liquide4_dose = $_POST["liquide4_dose"];
	$liquide5 = $_POST["liquide5"];
	$liquide5_dose = $_POST["liquide5_dose"];
	$liquide6 = $_POST["liquide6"];
	$liquide6_dose = $_POST["liquide6_dose"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va modifier la recette de la boisson dans la table Recette_tb. On modifie la recette indiquée par l'ID récupéré du formulaire et on remplace chaque champ par les informations du formulaire. Le premier champ prend la première variable, le deuxième champ prend la deuxième variable, etc...*/
	$requette_recette = $bdd->prepare('
		UPDATE Recette_tb SET RecetteName = :nom_boisson, BouteilleID1 = :liquide1, Quantity1 = :liquide1_dose, BouteilleID2 = :liquide2, Quantity2 = :liquide2_dose, BouteilleID3 = :liquide3, Quantity3 = :liquide3_dose, BouteilleID4 = :liquide4, Quantity4 = :liquide4_dose, BouteilleID5 = :liquide5, Quantity5 = :liquide5_dose, BouteilleID6 = :liquide6, Quantity6 = :liquide6_dose 
		WHERE RecetteID = :modif_boisson
	');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requette_recette->execute(array(
		'nom_boisson' => $nom_boisson,
		'liquide1' => $liquide1,
		'liquide1_dose' => $liquide1_dose,
		'liquide2' => $liquide2,
		'liquide2_dose' => $liquide2_dose,
		'liquide3' => $liquide3,
		'liquide3_dose' => $liquide3_dose,
		'liquide4' => $liquide4,
		'liquide4_dose' => $liquide4_dose,
		'liquide5' => $liquide5,
		'liquide5_dose' => $liquide5_dose,
		'liquide6' => $liquide6,
		'liquide6_dose' => $liquide6_dose,
		'modif_boisson' => $modif_boisson
	));

	/*Création de la requète qui va modifier la boisson dans la table Article_tb. On modifie l'article indiqué par l'ID de la recette récupéré du formulaire et on remplace chaque champ par les informations du formulaire. Le premier champ prend la première variable, le deuxième champ prend la deuxième variable, etc...*/
	$requete_article = $bdd->prepare('
		UPDATE Article_tb SET ArticleName = :nom_boisson, ArticlePrice = :prix_boisson, ArticleWeight = :volume_boisson 
		WHERE IDRecette = :modif_boisson
	');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete_article->execute(array(
		'nom_boisson' => $nom_boisson,
		'prix_boisson' => $prix_boisson,
		'volume_boisson' => $volume_boisson,
		'modif_boisson' => $modif_boisson
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Articles.php*/
	header('Location: IHM_Liste_Articles.php');
?>
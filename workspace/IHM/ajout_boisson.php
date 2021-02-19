<?php
/*Fonction php appelée par le formulaire d'ajout de boisson de la page IHM_Ajouter_Article.php, elle permet d'ajouter une boisson dans la table Article_tb de la base de données ainsi que sa recette associée grâce à son ID dans la table Recette_tb*/

	/*Récupération des données envoyées par le formulaire d'ajout de boisson*/
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
	
	/*Création de la requète qui va ajouter la recette de la boisson dans la table Recette_tb, le premier champ prend la première variable, le deuxième champ prend la deuxième variable, etc...*/
	$requete_recette = $bdd->prepare('
		INSERT INTO Recette_tb(RecetteName, BouteilleID1, Quantity1, BouteilleID2, Quantity2, BouteilleID3, Quantity3, BouteilleID4, Quantity4, BouteilleID5, Quantity5, BouteilleID6, Quantity6) 
		VALUES(:nom_boisson, :liquide1, :liquide1_dose, :liquide2, :liquide2_dose, :liquide3, :liquide3_dose, :liquide4, :liquide4_dose, :liquide5, :liquide5_dose, :liquide6, :liquide6_dose) 
	');

	/*On associe les variables de la requète avec les varaibles récupérées du formulaire*/
	$requete_recette->execute(array(
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
		'liquide6_dose' => $liquide6_dose
	));

	/*Requète qui permet de récupérer l'ID de la recette que l'on vient de créer*/
	$requete_ID = $bdd->query('
		SELECT RecetteID 
		FROM Recette_tb 
		WHERE RecetteID = (SELECT MAX(RecetteID) FROM Recette_tb)
	');
	$donnees = $requete_ID->fetch();
	$id_recette = $donnees['RecetteID'];

	/*Création de la requète qui va ajouter la nouvelle boisson dans la table Article_tb, le permier champ prend la première variable, le deuxième champ prend la deuxième variable, etc...*/	
	$requete_article = $bdd->prepare('
		INSERT INTO Article_tb(ArticleName, ArticlePrice, ArticleWeight, IDRecette) 
		VALUES(:nom_boisson, :prix_boisson, :volume_boisson, :id_recette)
	');

	/*On associe les variables de la requète avec les variables recupérées du formulaire*/
	$requete_article->execute(array(
		'nom_boisson' => $nom_boisson,
		'prix_boisson' => $prix_boisson,
		'volume_boisson' => $volume_boisson,
		'id_recette' => $id_recette
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Article.php*/
	header('Location: IHM_Liste_Articles.php');

?>
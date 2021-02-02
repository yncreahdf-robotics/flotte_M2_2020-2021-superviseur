<?php
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



	try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}

	$requete_recette = $bdd->prepare('INSERT INTO Recette_tb(RecetteName, BouteilleID1, Quantity1, BouteilleID2, Quantity2, BouteilleID3, Quantity3, BouteilleID4, Quantity4, BouteilleID5, Quantity5, BouteilleID6, Quantity6) VALUES(:nom_boisson, :liquide1, :liquide1_dose, :liquide2, :liquide2_dose, :liquide3, :liquide3_dose, :liquide4, :liquide4_dose, :liquide5, :liquide5_dose, :liquide6, :liquide6_dose) ');

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

	$requete_ID = $bdd->query('SELECT RecetteID FROM Recette_tb WHERE RecetteID = (SELECT MAX(RecetteID) FROM Recette_tb) ');
	$donnees = $requete_ID->fetch();
	$id_recette = $donnees['RecetteID'];

	
	$requete_article = $bdd->prepare('INSERT INTO Article_tb(ArticleName, ArticlePrice, ArticleWeight, IDRecette) VALUES(:nom_boisson, :prix_boisson, :volume_boisson, :id_recette) ');

	$requete_article->execute(array(
		'nom_boisson' => $nom_boisson,
		'prix_boisson' => $prix_boisson,
		'volume_boisson' => $volume_boisson,
		'id_recette' => $id_recette
	));

	header('Location: IHM_Liste_Articles.php');

?>
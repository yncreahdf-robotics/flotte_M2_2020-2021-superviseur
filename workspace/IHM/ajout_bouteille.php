<?php
	$nom_bouteille = $_POST["nom_bouteille"];
	$doseur = $_POST["doseur"];
	$emplacement = 0;


	try{
		$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
	}
	catch(Exception $e){
		die('Erreur : '.$e->getMessage());
	}

	$requete = $bdd->prepare('INSERT INTO Bouteille_tb(BouteilleName, VolumeDoseur, Emplacement) VALUES(:nom_bouteille, :doseur, :emplacement)');
	$requete->execute(array(
		'nom_bouteille' => $nom_bouteille,
		'doseur' => $doseur,
		'emplacement' => $emplacement
	));

	header('Location: IHM_Liste_Articles.php');
?>
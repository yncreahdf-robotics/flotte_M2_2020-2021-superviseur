<?php
	$nom_bouteille = $_POST["nom_bouteille"];
	$doseur = $_POST["doseur"];
	$emplacement = 0;

	include("connexion.php");

	$requete = $bdd->prepare('INSERT INTO Bouteille_tb(BouteilleName, VolumeDoseur, Emplacement) VALUES(:nom_bouteille, :doseur, :emplacement)');
	$requete->execute(array(
		'nom_bouteille' => $nom_bouteille,
		'doseur' => $doseur,
		'emplacement' => $emplacement
	));

	header('Location: IHM_Liste_Articles.php');
?>
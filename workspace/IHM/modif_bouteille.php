<?php
	$bouteille_modifiee = $_POST["bouteille_modifiee"];
	$nom_bouteille = $_POST["nom_bouteille"];
	$doseur = $_POST["doseur"];
	$emplacement = $_POST["emplacement"];

	include("connexion.php");

	if($emplacement != 0){
		$modif_emplacement = $bdd->prepare('UPDATE Bouteille_tb SET Emplacement = 0 WHERE Emplacement = :emplacement');
		$modif_emplacement->execute(array(
			'emplacement' => $emplacement
		));
	}

	$requete = $bdd->prepare('UPDATE Bouteille_tb SET BouteilleName = :nom_bouteille, VolumeDoseur = :doseur, Emplacement = :emplacement WHERE BouteilleID = :bouteille_modifiee');
	$requete->execute(array(
		'nom_bouteille' => $nom_bouteille,
		'doseur' => $doseur,
		'emplacement' => $emplacement,
		'bouteille_modifiee' => $bouteille_modifiee
	));

	header('Location: IHM_Liste_Articles.php');
?>
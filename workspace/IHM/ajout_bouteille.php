<?php
/*Fonction php appelée par le formulaire d'ajout de bouteille de la page IHM_Ajouter_Article.php, elle permet d'ajouter une bouteille dans la table Bouteille_tb de la base de donnée*/

	/*Récupération des données envoyées par le formulaire d'ajout de bouteille*/
	$nom_bouteille = $_POST["nom_bouteille"];
	$doseur = $_POST["doseur"];
	$emplacement = 0;

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va ajouter la bouteille dans la table Bouteille_tb, le premier champ prend la valeur de la première variable, le deuxième champ prend la valeur de la deuxième variable, etc...*/
	$requete = $bdd->prepare('
		INSERT INTO Bouteille_tb(BouteilleName, VolumeDoseur, Emplacement) 
		VALUES(:nom_bouteille, :doseur, :emplacement)
	');

	/*On associe les variables de la requète avec les variables récupérées du formulaire*/
	$requete->execute(array(
		'nom_bouteille' => $nom_bouteille,
		'doseur' => $doseur,
		'emplacement' => $emplacement
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Articles.php*/
	header('Location: IHM_Liste_Articles.php');
?>
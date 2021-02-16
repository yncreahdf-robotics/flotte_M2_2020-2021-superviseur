<?php
	
	/*Récupération de l'ID de la recette à supprimer depuis le formulaire*/
	$boisson_supprimee = $_POST["boisson_supprimee"];
	
	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*Création de la requète qui va supprimer la recette dans la table Recette_tb. On supprime la recette indiquée par l'ID récupéré du formulaire*/
	$requete_recette = $bdd->prepare('
		DELETE FROM Recette_tb 
		WHERE RecetteID = :boisson_supprimee
	');

	/*On associe la variable de la requète avec la variable récupérée du formulaire*/
	$requete_recette->execute(array(
		'boisson_supprimee' => $boisson_supprimee
	));

	/*Création de la requète qui va supprimer l'article dans la table Article_tb. On supprime l'article indiqué par l'ID de la recette associée récupéré par le formulaire*/
	$requette_article = $bdd->prepare('DELETE FROM Article_tb WHERE IDRecette = :boisson_supprimee');

	/*On associe la variable de la requète avec la variable récupérée du formulaire*/
	$requette_article->execute(array(
		'boisson_supprimee' => $boisson_supprimee
	));

	/*On renvoit l'utilisateur sur la page IHM_Liste_Articles.php*/ 
	header('Location: IHM_Liste_Articles.php');
?>
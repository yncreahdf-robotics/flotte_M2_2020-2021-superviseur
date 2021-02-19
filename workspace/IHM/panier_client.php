<?php
/*Fonction appelée lorsque le client veut ajouter un article sur la page IHM_Page_Client.php, elle ajoute l'article sélectionné avec la quantité saisie et elle modifie la table si besoin*/

	/*On démarre une session pour utiliser un panier associé au client*/
	session_start();	

	/*On récupère les fonctions de gestion du panier depuis le fichier fonctions_panier.php*/
	include_once("fonctions_panier.php");

	/*On vérifie que le panier est bien créer*/
	creationPanier();

	/*On récupère l'article choisit par le client avec le formulaire*/
	$_SESSION['panier']['table'] = $_POST["table"];
	$article_commande = $_POST["article_commande"];
	$quantite_article = $_POST["quantite_article"];

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*On récupère les informations de l'article sélectionné par le client pour l'ajouter au panier*/
	$requete = $bdd->prepare('
		SELECT ArticleID, ArticleName, ArticlePrice
		FROM Article_tb
		WHERE ArticleID = :article_commande
	');
	$requete->execute(array(
		'article_commande' => $article_commande
	));

	$article = $requete->fetch();

	/*On ajoute l'article au panier*/
	ajouterArticle($article['ArticleID'],$article['ArticleName'],$quantite_article,$article['ArticlePrice']);

	header('Location: IHM_Page_Client.php');
?>
<?php
/*Fonction appelée lorsque le client valide sa commande sur la page IHM_Commande_Client.php, elle envoit les articles commandés dans la table Commande_tb de la base de données*/

	/*On démarre une session pour utiliser un panier associé au client*/
	session_start();	

	/*On récupère les fonctions de gestion du panier depuis le fichier fonctions_panier.php*/
	include_once("fonctions_panier.php");

	/*On vérifie que le panier est bien créer*/
	creationPanier();	

	/*Connexion à la base de données avec le fichier connexion.php*/
	include("connexion.php");

	/*------------------------------ Création de la commande dans la bdd ------------------------------*/

	/*Création du numéro de commande, on vérifie que le numéro créé ne soit pas déjà attribué dans la bdd*/
	do{
		$creation_ok = true;
		$numero_commande = rand(1, 10000);
		$requette_nbr_cmd = $bdd->query('SELECT CommandNbr FROM Commande_tb');

		while($nrb_cmd = $requette_nbr_cmd->fetch()){
			if($nrb_cmd['CommandNbr'] === $numero_commande){
				$creation_ok = false;
				break;
			}
		}
	} while($creation_ok !== true);
	

	$etat = "Pending";
	$nombre_article = count($_SESSION['panier']['ID_article']);

	
	/*On ajoute les articles un par un dans la bdd (contrainte avec la structure de la bdd)*/
	for($i = 0; $i < $nombre_article; $i++){
		for($j = 0; $j < $_SESSION['panier']['quantite_produit'][$i]; $j++){
			/*Création de la requète qui va envoyer la commande dans la bdd*/
			$requette_commande = $bdd->prepare('
				INSERT INTO Commande_tb(CommandNbr, ArticleID, Etat)
				VALUES(:numero_commande, :ID_article, :etat)
			');
			/*On associe les variables de la requète avec les variables du panier*/
			$requette_commande->execute(array(
				'numero_commande' => $numero_commande,
				'ID_article' => $_SESSION['panier']['ID_article'][$i],
				'etat' => $etat
			));
		}
	}

	/*------------------------------ Mise à jour du prix de la table qui a passé la commande ------------------------------*/

	/*On récupère le montant à payer actuel de la table dans la bdd, la mise à zéro se fait manuellement depuis la page IHM_Suivi_Salle.php*/
	$requete_montant_actuel = $bdd->prepare('
		SELECT Prix
		FROM Table_tb
		WHERE TableID = :table
	');
	/*On associe les variables de la requète avec les variables du panier*/
	$requete_montant_actuel->execute(array(
		'table' => $_SESSION['panier']['table']
	));

	$montant_actuel = $requete_montant_actuel->fetch();

	$nouveau_montant = $montant_actuel['Prix'] + $_SESSION['panier']['montant_panier'];

	/*On met à jour le nouveau montant à payer de la table*/
	$requete_nouveau_montant = $bdd->prepare('
		UPDATE Table_tb
		SET Prix = :nouveau_montant, Etat = "Pending", CommandNbr = :numero_commande
		WHERE TableID = :table
	');
	/*On associe les varaibles de la requète avec les variables du panier*/
	$requete_nouveau_montant->execute(array(
		'nouveau_montant' => $nouveau_montant,
		'table' => $_SESSION['panier']['table'],
		'numero_commande' => $numero_commande
	));
	/*La commande étant envoyée, on supprime le panier*/
	supprimerPanier();

	/*On renvoit l'utilisateur sur la page IHM_Page_Client.php*/
	header('Location: IHM_Page_Client.php');
?>
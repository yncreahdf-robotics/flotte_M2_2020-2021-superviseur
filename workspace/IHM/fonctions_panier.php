<?php
/*Définitions des fonctions de gestion du panier*/

	/*Vérifie si le panier existe, le créer sinon*/
	function creationPanier(){
		if(!isset($_SESSION['panier'])){
			$_SESSION['panier'] = array();
		    $_SESSION['panier']['table'] = 0;
		    $_SESSION['panier']['ID_article'] = array();
		    $_SESSION['panier']['nom_produit'] = array();
		    $_SESSION['panier']['quantite_produit'] = array();
		    $_SESSION['panier']['prix_produit'] = array();
		    $_SESSION['panier']['montant_panier'] = 0;
		}
		return true;
	}



	/*Ajout d'un article dans le panier*/
	function ajouterArticle($IDArticle,$NomProduit,$QuantiteProduit,$PrixProduit){
		/*On vérifie que le panier existe*/
		if(creationPanier()){
			/*On regarde si le produit est déjà dans le panier et on ajout seulement la quantité si c'est le cas*/
			$positionProduit = array_search($IDArticle, $_SESSION['panier']['ID_article']);
			if($positionProduit !== false){
				$_SESSION['panier']['quantite_produit'][$positionProduit] += $QuantiteProduit;
			}
			/*Sinon on ajout le produit au panier*/
			else{
				array_push($_SESSION['panier']['ID_article'],$IDArticle);
				array_push($_SESSION['panier']['nom_produit'],$NomProduit);
				array_push($_SESSION['panier']['quantite_produit'],$QuantiteProduit);
				array_push($_SESSION['panier']['prix_produit'],$PrixProduit);
			}
		}
		else{
			echo "Un problème est survenu lors de l'ajout de l'article.";
		}
	}

	/*Modifie la quantité d'un article dans le panier*/
	function modifierQuantiteArticle(){

	}


	/*Supprime un article du panier*/
	function supprimerArticle(){

	}


	/*Calcul le montant total du panier*/
	function montantTotal(){
		$total = 0;
		$nombres_article = count($_SESSION['panier']['ID_article']);
		for($i = 0; $i < $nombres_article; $i++){
			$total = $total + ($_SESSION['panier']['quantite_produit'][$i] * $_SESSION['panier']['prix_produit'][$i]);
		}
		return $total;
	}

	/*Supprime le panier complet*/
	function supprimerPanier(){
		unset($_SESSION['panier']);
	}
?>
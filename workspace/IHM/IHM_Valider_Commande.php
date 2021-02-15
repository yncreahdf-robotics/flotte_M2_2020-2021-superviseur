<?php 
	session_start();	/*On démarre une session pour utiliser un panier associé au client*/
	//include_once("fonctions-panier.php");
?>


<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Validation de la commande</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<!-- Affichage du panier -->
			<section>
				<h2>Commande en cours</h2>
				<h2><br />Liste des articles sélectionnés :</h2>
				<?php
					for($i = 0; $i < count($_SESSION['panier']['nom_produit']); $i++){
						echo $_SESSION['panier']['nom_produit'][$i] . " - Quantité : " . $_SESSION['panier']['quantite_produit'][$i] . " - Prix unitaire : " . $_SESSION['panier']['prix_produit'][$i] . "€<br />";
					}
				?>
				<p>
					Table : <?php echo $_SESSION['panier']['table'] ?><br />
					Prix total : <?php echo montantTotal() ?>€
				</p>
				<nav>
					<div class="bouton" id="valider">
						<p>Valider la commande</p>
					</div>
					<div class="bouton" id="appel_serveur">
						<h3>Appeler un serveur</h3>
					</div>
				</nav>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_ret = document.getElementById('Retour');
			elt_ret.addEventListener('click', function retour(event){
				//event.preventDefault()
				document.location = "IHM_Page_Client.php";
			})


			//Bouton de retour à l'accueil client
			const elt_retour = document.getElementById('retour');
			elt_retour.addEventListener('click', function client(event){
				//event.preventDefault()
				document.location = "IHM_Page_Client.php";
			})
		</script>
	</body>
</html>
<?php 
	session_start();	//On démarre une session pour utiliser un panier associé au client
	include_once("fonctions-panier.php");
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
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Commande validée avec succès !</h2>
				<h2 class="Commande"><br />Liste des articles commandés :</h2>
				<ul class="Commande">
					<li>Article 1  -  Quantité : X  -  Prix unitaire : €  -  Prix total : €</li>
					<br />
					<li>Article 2  -  Quantité : X  -  Prix unitaire : €  -  Prix total : €</li>
					<br />
					<li>Article 3  -  Quantité : X  -  Prix unitaire : €  -  Prix total : €</li>
				</ul>
				<p class="Commande">
					Prix total : €
				</p>
				<nav>
					<div class="bouton" id="retour">
						<h3><a href="IHM_Page_Client.php">Retour à l'accueil</a></h3>
					</div>
				</nav>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_ret = document.getElementById('Retour');
			elt_ret.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Commande_Client.php";
			})


			//Bouton de retour à l'accueil client
			const elt_retour = document.getElementById('retour');
			elt_retour.addEventListener('click', function client(event){
				event.preventDefault()
				document.location = "IHM_Page_Client.php";
			})
		</script>
	</body>
</html>
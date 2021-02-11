<?php
	session_start();	/*On démarre une session pour utiliser un panier associé au client*/
	//include_once("fonctions-panier.php");
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Commande client en cours</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Commande en cours</h2>
				<h2 class="Commande"><br />Liste des articles sélectionnés :</h2>
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
			//Validation de la commande
			const elt_valider = document.getElementById('valider');
			elt_valider.addEventListener('click', function valider_commande(event) {
				//event.preventDefault();
				if(confirm("Valider la commande ?")){
					document.location = "IHM_Valider_Commande.php";
				}
				else{
					
				}
			})

			//Appel d'un serveur
			const elt = document.getElementById('appel_serveur');
			elt.addEventListener('click', function appel_serveur(event) {
				//event.preventDefault()
				if(confirm("Etes-vous sur de vouloir appeler un serveur ?")){
					alert("Un serveur a été appelé.")
				}
				else{
					
				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function client(event){
				//event.preventDefault()
				document.location = "IHM_Page_Client.php";
			})
		</script>
	</body>
</html>
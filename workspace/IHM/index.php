<?php
	/*Page d'accueil du site, elle donne accès à la partie client et à la partie propriétaire. Ce nom de fichier est nécessaire pour que le serveur sache quel fichier appeler en premier lorsqu'on démarre le site*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>FRS - Accueil</title>
	</head>

	<body>
		<div id="bloc_page">

			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>

			<section>
				<h2>Accueil</h2>

				<!-- Création de boutons permettant d'accèder à la partie propriétaire ou à la partie client du site -->
				<nav>
					<div class="bouton" id="proprietaire">
						<p>Menu Proprietaire</p>
					</div>
					<div class="bouton" id="client">
						<p>Menu Client</p>
					</div>
				</nav>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton pour accèder à la page de protection de la partie propriétaire
			const elt_password = document.getElementById('proprietaire');
			elt_password.addEventListener('click', function mot_de_passe(event){
				document.location = "IHM_Mot_De_Passe.php";
			})

			//Bouton pour interface client
			const elt_client = document.getElementById('client');
			elt_client.addEventListener('click', function client(event){
				document.location = "IHM_Page_Client.php";
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				document.location = "index.php";
			})
		</script>
	</body>
</html>
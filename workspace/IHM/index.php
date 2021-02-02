<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>FRS - Accueil</title>
	</head>

	<body>
		<div id="bloc_page">

			<?php include("entete.php"); ?>

			<section>
				<h2>Accueil</h2>
				<nav>
					<div class="bouton" id="proprietaire">
						<h3><a href="IHM_Mot_De_Passe.php">Menu Proprietaire</a></h3>
					</div>
					<div class="bouton" id="client">
						<h3><a href="IHM_Page_Client.php">Menu Client</a></h3>
					</div>
				</nav>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>

		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton pour accèder à la page de protection de la partie propriétaire
			const elt_password = document.getElementById('proprietaire');
			elt_password.addEventListener('click', function mot_de_passe(event){
				event.preventDefault()
				document.location = "IHM_Mot_De_Passe.php";
			})

			//Bouton pour interface client
			const elt_client = document.getElementById('client');
			elt_client.addEventListener('click', function client(event){
				event.preventDefault()
				document.location = "IHM_Page_Client.php";
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Accueil.php";
			})
		</script>
	</body>
</html>
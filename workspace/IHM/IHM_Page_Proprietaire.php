<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Accueil Proprietaire</title>
	</head>
	
	<body>
		<div id="bloc_page">
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Menu Proprietaire</h2>
				<nav>
					<div class="bouton" id="suivi">
						<h3><a href="IHM_Suivi_Salle.php">Suivi de la salle</a></h3>
					</div>
					<div class="bouton" id="liste_robot">
						<h3><a href="IHM_Liste_Robots.php">Liste des Robots</a></h3>
					</div>
					<div class="bouton" id="liste_article">
						<h3><a href="IHM_Liste_Articles.php">Liste des Articles</a></h3>
					</div>
					<div class="bouton" id="liste_commande">
						<h3><a href="IHM_Liste_Commandes.php">Liste des Commandes</a></h3>
					</div>
					<div class="bouton" id="liste_position">
						<h3><a href="IHM_Liste_Positions.php">Liste des Positions</a></h3>
					</div>
					<div class="bouton" id="deplacer_robot">
						<h3><a href="IHM_Deplacer_Robot.php">Appeler ou envoyer un robot</a></h3>
					</div>
				</nav>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "index.php";
			})

			//Bouton suivi de salle
			const elt_suivi = document.getElementById('suivi');
			elt_suivi.addEventListener('click', function suivi(event){
				event.preventDefault()
				document.location = "IHM_Suivi_Salle.php";
			})

			//Bouton liste des robots
			const elt_liste_robot = document.getElementById('liste_robot');
			elt_liste_robot.addEventListener('click', function liste_robot(event){
				event.preventDefault()
				document.location = "IHM_Liste_Robots.php";
			})

			//Bouton liste des articles
			const elt_liste_article = document.getElementById('liste_article');
			elt_liste_article.addEventListener('click', function liste_article(event){
				event.preventDefault()
				document.location = "IHM_Liste_Articles.php";
			})

			//Bouton liste des commandes
			const elt_liste_commande = document.getElementById('liste_commande');
			elt_liste_commande.addEventListener('click', function liste_commande(event){
				event.preventDefault()
				document.location = "IHM_Liste_Commandes.php";
			})

			//Bouton liste des positions
			const elt_liste_position = document.getElementById('liste_position');
			elt_liste_position.addEventListener('click', function liste_position(event){
				event.preventDefault()
				document.location = "IHM_Liste_Positions.php";
			})

			//Bouton envoi de robot
			const elt_envoi_robot = document.getElementById('deplacer_robot');
			elt_envoi_robot.addEventListener('click', function deplacer_robot(event){
				event.preventDefault()
				document.location = "IHM_Deplacer_Robot.php";
			})
		</script>
	</body>
</html>
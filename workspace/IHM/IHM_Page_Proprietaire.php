<?php
	/*Page du menu de la partie propriétaire, elle donne accès aux différents outils de gestions de la base de données, de la salle ou des robots.*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Accueil Proprietaire</title>
	</head>
	
	<body>
		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php-->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Menu Proprietaire</h2>
				<!-- Création de boutons permettant d'accèder aux différentes pages de la partie propriétaire -->
				<nav>
					<div class="bouton" id="suivi">
						<p>Suivi de la salle</p>
					</div>
					<div class="bouton" id="liste_robot">
						<p>Liste des Robots</p>
					</div>
					<div class="bouton" id="liste_article">
						<p>Liste des Articles</p>
					</div>
					<div class="bouton" id="liste_commande">
						<p>Liste des Commandes</p>
					</div>
					<div class="bouton" id="liste_position">
						<p>Liste des Positions</p>
					</div>
					<div class="bouton" id="deplacer_robot">
						<p>Appeler ou envoyer un robot</p>
					</div>
				</nav>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php-->
			<?php include("pied_de_page.php"); ?>
		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				document.location = "index.php";
			})

			//Bouton suivi de salle
			const elt_suivi = document.getElementById('suivi');
			elt_suivi.addEventListener('click', function suivi(event){
				document.location = "IHM_Suivi_Salle.php";
			})

			//Bouton liste des robots
			const elt_liste_robot = document.getElementById('liste_robot');
			elt_liste_robot.addEventListener('click', function liste_robot(event){
				document.location = "IHM_Liste_Robots.php";
			})

			//Bouton liste des articles
			const elt_liste_article = document.getElementById('liste_article');
			elt_liste_article.addEventListener('click', function liste_article(event){
				document.location = "IHM_Liste_Articles.php";
			})

			//Bouton liste des commandes
			const elt_liste_commande = document.getElementById('liste_commande');
			elt_liste_commande.addEventListener('click', function liste_commande(event){
				document.location = "IHM_Liste_Commandes.php";
			})

			//Bouton liste des positions
			const elt_liste_position = document.getElementById('liste_position');
			elt_liste_position.addEventListener('click', function liste_position(event){
				document.location = "IHM_Liste_Positions.php";
			})

			//Bouton envoi de robot
			const elt_envoi_robot = document.getElementById('deplacer_robot');
			elt_envoi_robot.addEventListener('click', function deplacer_robot(event){
				document.location = "IHM_Deplacer_Robot.php";
			})
		</script>
	</body>
</html>
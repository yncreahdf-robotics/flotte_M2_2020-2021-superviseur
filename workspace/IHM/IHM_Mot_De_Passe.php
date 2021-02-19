<?php
	/*Page permettant de limiter l'accès à la partie propriétaire grâce à un mot de passe, elle fait appel à mot_de_passe.php pour faire la vérification des identifiants saisis par l'utilisateur*/
?>	

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="IHM.css" />
		<title>Vérification d'accès</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>

			<h1>Saisir les identifiants pour accèder à la partie propriétaire</h1>
			<!-- Formulaire qui permet de saisir l'identifiant et le mot de passe pour accéder à la partie propriétaire -->
			<form action="mot_de_passe.php" method="post">
				<p>
					Nom d'utilisateur : <br /><input type="text" name="username" />
					<br />
					<br />
	        		Mot de passe : <br /><input type="password" name="password" />
	        		<br />
	        		<br />
	        		<input type="submit" id="submit" value="Connexion" />
				</p>
			</form>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
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
		</script>
	</body>
</html>
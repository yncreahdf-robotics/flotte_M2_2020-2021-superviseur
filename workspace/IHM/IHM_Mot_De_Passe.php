<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" href="IHM.css" />
		<title>Vérification d'accès</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<?php include("entete.php"); ?>

			<h1>Saisir les identifiants pour accèder à la partie propriétaire</h1>
			<form action="mot_de_passe.php" method="post">
				<p>
					Nom d'utilisateur : <br /><input type="text" name="username" /><br /><br />
	        		Mot de passe : <br /><input type="password" name="password" /><br /><br />
	        		<input type="submit" id="submit" value="Connexion" />
				</p>
			</form>

		<?php include("pied_de_page.php"); ?>

		</div>


		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Accueil.php";
			})
		</script>
	</body>
</html>
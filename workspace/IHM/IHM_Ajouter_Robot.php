<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Ajouter un robot</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Saisir le nom du nouveau type de robot</h2>
				<form method="post" action="ajout_type_robot.php">
    				<p>
        				<label for="type_robot">Type de robot :</label>
        				<input type="text" name="type_robot" id="type_robot" placeholder="Ex : Robotino" size="35" maxlength="30" />
        				<br /><br />
        				<label for="role">Role du robot :</label>
        				<select name="role" id="role">
        					<option value="Service">Service</option>
        					<option value="Guide">Guide</option>
        					<option value="Preparateur">Preparateur</option>
        					<option value="Melangeur">Melangeur</option>
        					<option value="Manipulateur">Manipulateur</option>
        					<option value="Accueil">Accueil</option>
        				</select>
        				<br /><br />
        				<label for="weight_capacity">Poids supporté maximal (en g):</label>
        				<input type="number" name="weight_capacity" id="weight_capacity" min="-1" step="1" />
   					</p>
   					<br />
   					<input type="submit" value="Valider" id="valider" />
   					<br />
				</form>
				
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			const elt = document.getElementById('valider');
			elt.addEventListener('click', function valider(event) {
				alert("Type de robot ajouté.");
				document.location = "IHM_Liste_Robots.php";
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Liste_Robots.php";
			})
		</script>
	</body>
</html>
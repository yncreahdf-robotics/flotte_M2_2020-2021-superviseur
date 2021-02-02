<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Ajouter une position</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Définir une nouvelle position</h2>
				<form method="post" action="ajout_position.php">
    				<p>
        				<label for="nom_position">Nom de la position :</label>
        				<input type="text" name="nom_position" id="nom_position" placeholder="Ex : Table1" size="30" maxlength="10" />
        				<br />
        				<br />
        				<label for="position_X">Position en X :</label>
        				<input type="number" name="position_X" id="position_X" placeholder="Ex : 2.45" step="0.01" />
        				<br />
        				<br />
        				<label for="position_Y">Position en Y :</label>
        				<input type="number" name="position_Y" id="position_Y" placeholder="Ex : -0.34" step="0.01" />
        				<br />
        				<br />
        				<label for="position_Z">Position en Z :</label>
        				<input type="number" name="position_Z" id="position_Z" placeholder="Ex : 1.67" step="0.01" />
        				<br />
        				<br />
        				<label for="position_W">Position en W :</label>
        				<input type="number" name="position_W" id="position_W" placeholder="Ex : 0.80" step="0.01" />
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
				alert("Article ajouté.");
				document.location = "IHM_Liste_Positions.php";
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Liste_Positions.php";
			})
		</script>
	</body>
</html>
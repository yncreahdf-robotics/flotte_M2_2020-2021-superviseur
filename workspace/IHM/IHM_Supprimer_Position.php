<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Supprimer une position</title>
	</head>

	<body>
		<div id="bloc_page">
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Sélectionner la position à supprimer</h2>
				<form method="post" action="supprimer_position.php">
   					<p>
   						<?php
       						while($donnees = $requete->fetch()){
       							echo "<input type=\"radio\" name=\"selected_position\" value=\"".$donnees['PoseID']."\" id=\"".$donnees['PoseName']."\"/><label for=\"".$donnees['PoseName']."\">".$donnees['PoseName']."</label>" ;
       					?>
       					<br />
       					<br />
       					<?php
       						}
       					?>
       					<input type="submit" name="Supprimer" value="Supprimer" id="supprimer" />
   					</p>
				</form>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			const elt = document.getElementById('supprimer');
			elt.addEventListener('click', function supprimer(event) {
				event.preventDefault()
				if(confirm("Etes-vous sur de vouloir supprimer cette position ?")){
					alert("La position a été supprimée");
					document.location = "IHM_Liste_Positions.php";
				}
				else{

				}
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
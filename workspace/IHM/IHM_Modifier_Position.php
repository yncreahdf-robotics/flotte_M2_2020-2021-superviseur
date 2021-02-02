<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Modifier une position</title>
	</head>

	<body>
		<div id="bloc_page">
			<?php
				
				include("connexion.php");
				
				$requete = $bdd->query('SELECT * FROM Pose_tb');
			?>
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Sélectionner la position à modifier</h2>
				<form method="post" action="modif_position.php">
   					<p>
   						<?php
       						while($donnees = $requete->fetch()){
       							echo "<input type=\"radio\" name=\"selected_position\" value=\"".$donnees['PoseID']."\" id=\"".$donnees['PoseID']."\"/><label for=\"".$donnees['PoseID']."\">".$donnees['PoseName']."</label>" ;
       					?>
       					<br />
       					<br />
       					<?php
       						}
       					?>
   					</p>
				

				<h2>Saisir les nouvelles informations</h2>
				
    				<p>
        				<label for="nom_position">Nom de la position :</label>
        				<input type="text" name="new_nom_position" id="nom_position" size="30" maxlength="10" />
        				<br />
        				<br />
        				<label for="position_X">Position en X :</label>
        				<input type="number" name="new_position_X" id="position_X" step="0.01" />
        				<br />
        				<br />
        				<label for="position_Y">Position en Y :</label>
        				<input type="number" name="new_position_Y" id="position_Y" step="0.01" />
        				<br />
        				<br />
        				<label for="position_Z">Position en Z :</label>
        				<input type="number" name="new_position_Z" id="position_Z" step="0.01" />
        				<br />
        				<br />
        				<label for="position_W">Position en W :</label>
        				<input type="number" name="new_position_W" id="position_W" step="0.01" />
        				<br />
        				<br />
        				<input type="submit" name="Modifier" value="Modifier" id="modifier" />
   					</p>
				</form>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
		<script type="text/javascript">
			//Bouton validant les modifications
			const elt = document.getElementById('modifier');
			elt.addEventListener('click', function modifier(event) {
				event.preventDefault()
				if(confirm("Appliquer les modifications ?")){
					alert("La position a été modifiée.")
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

			//Fonction d'auto-remplissage des champs
			/*<?php
				while($donnees = $requete->fetch()){
			?>
				$(document).ready(function(){
					$("#<?php echo $donnees['PoseName'] ;?>").click(function(){
			    		$("#nom_position").attr("value","<?php echo $donnees['PoseName'] ;?>");
			    		$("#position_X").attr("value","<?php echo $donnees['PoseX'] ;?>");
			    		$("#position_Y").attr("value","<?php echo $donnees['PoseY'] ;?>");
			    		$("#position_Z").attr("value","<?php echo $donnees['PoseZ'] ;?>");
			    		$("#position_W").attr("value","<?php echo $donnees['PoseW'] ;?>");
			  		});
				});
			<?php
				}
			?>*/
		</script>
	</body>
</html>
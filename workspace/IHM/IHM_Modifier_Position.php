<?php
	/*Page permettant de saisir les nouvelles informations d'une position déjà présente dans la base de données avec le formulaire appelant modif_position.php*/
?>

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
				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");
				
				/*Création de la requète qui récupère les informations des positions dans Pose_tb*/
				$requete = $bdd->query('SELECT * FROM Pose_tb');
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Sélectionner la position à modifier</h2>
				<!-- Formulaire qui permet de modifier les informations d'une position -->
				<form method="post" action="modif_position.php">
   					<p>
   						<?php
   						/*On récupère les informations depuis requete et on les affiches dans une liste de boutons radio. Chaque recette va créer une option dans la liste. Cette liste permet de choisir la recette qui sera modifiée grâce à son ID*/
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
    					<!-- Saisie des nouvelles informations de la position -->
        				<label for="nom_position">Nom de la position :</label>
        				<input type="text" name="new_nom_position" id="nom_position" size="30" maxlength="30" />
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

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
		<script type="text/javascript">
			//Bouton validant les modifications
			const elt = document.getElementById('modifier');
			elt.addEventListener('click', function modifier(event) {
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
				document.location = "IHM_Liste_Positions.php";
			})
		</script>
	</body>
</html>
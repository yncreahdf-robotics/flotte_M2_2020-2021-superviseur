<?php
	/*Page permettant de supprimer une position de la base de données avec le formulaire appelant supprimer_position.php*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Supprimer une position</title>
	</head>

	<body>
		<div id="bloc_page">

			<?php 

				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");

				/*Création de la requète qui va récupérer l'ID et le nom des positions depuis la table Pose_tb*/
				$requete = $bdd->query('
					SELECT PoseID, PoseName 
					FROM Pose_tb
				');
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Sélectionner la position à supprimer</h2>
				<!-- Formulaire permettant de supprimer une position de la table Pose_tb -->
				<form method="post" action="supprimer_position.php">
   					<p>
   						<?php
   						/*On récupère les informations depuis requete et on affiche les affiche dans une liste de boutons radio. Chaque position va créer une option dans la liste. Cette liste permet de choisir la position que l'on va supprimer*/
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

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de validation de suppression
			const elt = document.getElementById('supprimer');
			elt.addEventListener('click', function supprimer(event) {
				//event.preventDefault()
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
				//event.preventDefault()
				document.location = "IHM_Liste_Positions.php";
			})
		</script>
	</body>
</html>
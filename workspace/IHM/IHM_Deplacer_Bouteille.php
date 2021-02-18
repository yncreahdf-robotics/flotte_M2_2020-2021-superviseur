<?php
	/*Page qui permet de déplacer une bouteille en la sélectionnant et en choisissant sa nouvelle position avec le formulaire. Ce formulaire va appeler deplacer_bouteille.php pour effectuer les modifications*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Gestion Tourniquet</title>
	</head>
	<body>

		<?php

			/*Connexion à la base de données avec le fichier connexion.php*/
			include("connexion.php");

			/*Création de la requète qui va récupérer l'ID, le nom et l'emplacement des bouteilles dans la table Bouteille_tb. On ne recupère pas l'ID = 0 car c'est un champ servant à indiquer qu'il n'y a pas de bouteille*/
			$requete_bouteille = $bdd->query('
				SELECT BouteilleID, BouteilleName, Emplacement
				FROM Bouteille_tb
				WHERE BouteilleID <> 0 AND BouteilleID <> 1
			 ')
		?>

		<div id="bloc_page">

			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>

			<h3>Sélectionner la bouteille à déplacer</h3>
			<form method="post" action="deplacer_bouteille.php">
				<p>
					<select name="bouteille_modifiee" id="bouteille_modifiee">
					<?php
					/*On récupère les informations depuis requete_bouteille et on les affiches dans une liste déroulante. Chaque bouteille va créer une noption dans la liste. Cette liste permet de choisir la bouteille qui sera modifiée grâce à son ID*/
						while($bouteilles = $requete_bouteille->fetch()){
							echo "<option value=\"" . $bouteilles['BouteilleID'] . "\">" . $bouteilles['BouteilleName'] . "</option>";
		        		}
						?>
					</select>
				</p>

				<h3>Saisir les nouvelles informations</h3>
				<p>
					<label for="emplacement">Emplacement de la bouteille :</label>
	        		<select name="emplacement" id="emplacement">
	        			<option value="0"> Pas sur le tourniquet </option>
	        			<option value="1"> Emplacement 1 </option>
	        			<option value="2"> Emplacement 2 </option>
	        			<option value="3"> Emplacement 3 </option>
	        			<option value="4"> Emplacement 4 </option>
	        			<option value="5"> Emplacement 5 </option>
	        			<option value="6"> Emplacement 6 </option>
	        		</select>
	        		<br />
	        		<br />
	        		<input type="submit" name="modif_bouteille_ok" value="Déplacer" id="modif_ok" />
	   			</p>
	   		</form>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>
		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de validation d'une modification
			const elt = document.getElementById('modif_ok');
			elt.addEventListener('click', function modifier(event) {
				if(confirm("Appliquer les modifications ?")){
					alert("L'article a été modifié.")
					document.location = "IHM_Liste_Articles.php";
				}
				else{

				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				document.location = "IHM_Suivi_Salle.php";
			})
		</script>
	</body>
</html>
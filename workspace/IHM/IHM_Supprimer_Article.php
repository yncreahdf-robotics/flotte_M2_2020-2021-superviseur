<?php
	/*Page permettant de supprimer une boisson ou une bouteille de la base de données avec les formulaires appelant respectivement supprimer_boisson.php ou supprimer_bouteille.php*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Supprimer un article</title>

		<!-- Fonctions qui permettent d'afficher le formulaire de suppression d'une bouteille OU d'une boisson -->
		<script type="text/javascript">
			function aff_bouteille(action){
    			document.getElementById('block_bouteille').style.display = (action == "oui")? "inline" : "none";
			}
			function aff_boisson(action){
    			document.getElementById('block_boisson').style.display= (action == "oui")? "inline" : "none";
			}
		</script>
	</head>

	<body>
		<div id="bloc_page">

			<?php

				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");

				/*Création de la requète qui va récupérer les informations des bouteilles dans la table Bouteille_td. On ne récupère pas la bouteille avec un ID de 0 car c'est un champ servant à indiquer qu'il n'y a pas de bouteille*/
				$requete_bouteille = $bdd->query('SELECT * FROM Bouteille_tb WHERE BouteilleID <> 0');	
						
				/*Création de la requète qui va récupérer les noms et les ID des recettes dans la table Recette_tb*/
					$requete_recette = $bdd->query('
					SELECT RecetteID, RecetteName 
					FROM Recette_tb
				');
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.phph -->
			<?php include("entete.php"); ?>
		
			<section>

				<!-- Permet de choisir entre une suppression de boisson et une suppression de bouteille grâce à l'appel des fonctions définies en début de page -->
				<div id="Choix_ajout">
					<h3>Que voulez vous supprimer ?</h3>
					<input type="radio" name="Choix_ajout" value="Bouteille" onchange="aff_bouteille('oui'); aff_boisson('non')" /><label class="label-radio">Une bouteille</label><br/>
		        	<input type="radio" name="Choix_ajout" value="Boisson" onchange="aff_bouteille('non'); aff_boisson('oui')" /><label class="label-radio">Une boisson</label><br/><br/>
				</div>


<!-- ------------------------------------------------------------ Suppression d'une bouteille ------------------------------------------------------------ -->
				<div id="block_bouteille" hidden="hidden">
					<h3>Sélectionner la bouteille à supprimer</h3>
					<!-- Formulaire qui permet de supprimer une bouteille de la table Bouteille_tb -->
					<form method="post" action="supprimer_bouteille.php">
						<select name="bouteille_supprimee" id="bouteille_supprimee">
							<?php 
							/*On récupère les informations depuis requete_bouteille et on les affiche dans une liste déroulante. Chaque bouteille va créer une option dans la liste. Cette liste permet de choisir quelle bouteille on va supprimer*/
								while($bouteilles = $requete_bouteille->fetch()){
									echo "<option value=\"" . $bouteilles['BouteilleID'] . "\">" . $bouteilles['BouteilleName'] . "</option>";
	        					}
							?>
						</select>
						<br />
						<br />
						<input type="submit" name="Supprimer" value="Supprimer" />
					</form>
				</div>

<!-- ------------------------------------------------------------ Suppression d'une boisson ------------------------------------------------------------ -->
				<div id="block_boisson" hidden="hidden">
					<h3>Sélectionner l'article à supprimer</h3>
					<!-- Formulaire qui permet de supprimer une boisson des tables Article_tb et Recette_tb grâce à l'ID des recettes communs aux deux tables -->
					<form method="post" action="supprimer_boisson.php">
						<select name="boisson_supprimee" id="boisson_supprimee">
							<?php
							/*On récupère les informations depuis requete_recette et on les affiche dans une liste déroulante. CHaque recette va créer une option dans la liste? Cette liste permet de choisir quelle recette on va supprimer*/
								while($articles = $requete_recette->fetch()){
									echo "<option value=\"" . $articles['RecetteID'] . "\">" . $articles['RecetteName'] . "</option>";
								}
							?>
						</select>
						<br />
						<br />
						<input type="submit" name="Supprimer" value="Supprimer " id="supprimer" />
					</form>
				</div>
				<br />
				<br />
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de validation de la suppression 
			const elt = document.getElementById('supprimer');
			elt.addEventListener('click', function supprimer(event) {
				//event.preventDefault()
				if(confirm("Etes-vous sur de vouloir supprimer cet article ?")){
					alert("L'article a été supprimé");
					document.location = "IHM_Liste_Articles.php";
				}
				else{
					
				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				//event.preventDefault()
				document.location = "IHM_Liste_Articles.php";
			})
		</script>
	</body>
</html>
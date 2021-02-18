<?php
	/*Page qui permet de saisir les informations d'une nouvelle bouteille ou d'une nouvelle boisson qui seront ajoutées à la base de données avec les formulaires appelant respectivement ajout_bouteille.php ou ajout_boisson.php*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Ajouter un article</title>

		<!-- Fonctions qui permettent d'afficher le formulaire d'ajout d'une bouteille OU d'une boisson -->
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

				/*Création de 6 requètes qui vont toutes récupérer l'ID et le nom des bouteilles depuis la base de données, il faut 6 requètes car on peut avoir jusqu'à 6 bouteilles dans une même boisson*/
				$requete1 = $bdd->query('SELECT BouteilleID, BouteilleName FROM Bouteille_tb ORDER BY BouteilleID');
				$requete2 = $bdd->query('SELECT BouteilleID, BouteilleName FROM Bouteille_tb ORDER BY BouteilleID');
				$requete3 = $bdd->query('SELECT BouteilleID, BouteilleName FROM Bouteille_tb ORDER BY BouteilleID');
				$requete4 = $bdd->query('SELECT BouteilleID, BouteilleName FROM Bouteille_tb ORDER BY BouteilleID');
				$requete5 = $bdd->query('SELECT BouteilleID, BouteilleName FROM Bouteille_tb ORDER BY BouteilleID');
				$requete6 = $bdd->query('SELECT BouteilleID, BouteilleName FROM Bouteille_tb ORDER BY BouteilleID');
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Saisir les informations de la nouvelle bouteille ou de la nouvelle boisson</h2>
				<br />

				<!-- Permet de choisir entre un ajout de boisson et un ajout de bouteille grâce à l'appel des fonctions définies en début de page -->
				<div id="Choix_ajout">
					<h3>Que voulez vous ajouter ?</h3>
					<input type="radio" name="Choix_ajout" value="Bouteille" onchange="aff_bouteille('oui'); aff_boisson('non')" />
					<label for="Bouteille" class="label-radio">Une bouteille</label>
					<br/>
		        	<input type="radio" name="Choix_ajout" value="Boisson" onchange="aff_bouteille('non'); aff_boisson('oui')" />
		        	<label for="Boisson" class="label-radio">Une boisson</label>
		        	<br/>
		        	<br/>
				</div>

<!-- --------------------------------------------------------------- Ajout d'une bouteille --------------------------------------------------------------- -->
				<!-- Formulaire qui permet de rentrer les informations d'une nouvelle bouteille -->
				<div id="block_bouteille" hidden="hidden">
					<form method="post" action="ajout_bouteille.php">
	    				<p>
	        				<label for="nom_bouteille">Nom de la bouteille :</label>
	        				<input type="text" name="nom_bouteille" id="nom_bouteille" placeholder="Ex : Ice Tea" size="30" maxlength="20" />
	        				<br />
	        				<br />
	        				<label for="doseur">Doseur associé à la bouteille :</label>
	        				<select name="doseur" id="doseur">
	        					<option value="25">25 mL</option>
	        					<option value="35">35 mL</option>
	        					<option value="50">50 mL</option>
	        				</select>
	        				<br />
	        				<br />
	        				<input type="submit" value="Valider" id="valider">
	        				<br />
	   					</p>
					</form>
				</div>


<!-- --------------------------------------------------------------- Ajout d'une boisson --------------------------------------------------------------- -->
				<!-- Formulaire qui permet de rentrer les informations d'une nouvelle boisson -->
				<div id="block_boisson" hidden="hidden">
					<form method="post" action="ajout_boisson.php">
	    				<p>	<!-- Informations de base de la boisson qui seront envoyées dans la table des articles -->
	        				<label for="nom_boisson">Nom de la boisson :</label>
	        				<input type="text" name="nom_boisson" id="nom_boisson" size="30" maxlength="30" />
	        				<br />
	        				<br />
	        				<label for="prix_boisson">Prix (€) :</label>
	        				<input type="number" name="prix_boisson" id="prix_boisson" min="0" step="0.01" />
	        				<br />
	        				<br />
	        				<label for="volume_boisson">Volume (cL) :</label>
	        				<input type="number" name="volume_boisson" id="volume_boisson" min="0" step="1" />
	        				<br />
	        				<br />
	        				<!-- Compositions de la boisson qui sera envoyée dans la table des recettes, en plus du nom de la boisson -->
	        				<h3>Composition de la boisson :</h3>
	        				<label for="liquide1">Premier liquide à verser : </label>
	        				<select name="liquide1" id="liquide1">
	        					<?php
	        					/*On affiche toutes les bouteilles disponibles dans la base de données dans une liste déroulante et on récupère l'ID de la bouteille qui sera envoyée par le formulaire et on indique le nombre de dose*/
	        						while($donnees = $requete1->fetch()){
	        							echo "<option value=\"" . $donnees['BouteilleID'] . "\">" . $donnees['BouteilleName'] . "</option>";
	        						}
	        					?>
	        				</select>
	        				<label for="liquide1_dose"> Nombre de dose :</label>
	        				<input type="number" name="liquide1_dose" id="liquide1_dose" min="0" max="5" size="10" value="0" />
	        				
	        				<br />
	        				<br />

	        				<label for="liquide2">Deuxième liquide à verser : </label>
	        				<select name="liquide2" id="liquide2" />
	        					<?php
	        					/*On affiche toutes les bouteilles disponibles dans la base de données dans une liste déroulante et on récupère l'ID de la bouteille qui sera envoyée par le formulaire et on indique le nombre de dose*/
	        						while($donnees2 = $requete2->fetch()){
	        							echo "<option value=\"" . $donnees2['BouteilleID'] . "\">" . $donnees2['BouteilleName'] . "</option>";
	        						}
	        					?>
	        				</select>
	        				<label for="liquide2_dose"> Nombre de dose :</label>
	        				<input type="number" name="liquide2_dose" id="liquide2_dose" min="0" max="5" size="10" value="0" />
	        				
	        				<br />
	        				<br />

	        				<label for="liquide3">Troisième liquide à verser : </label>
	        				<select name="liquide3" id="liquide3" />
	        					<?php
	        					/*On affiche toutes les bouteilles disponibles dans la base de données dans une liste déroulante et on récupère l'ID de la bouteille qui sera envoyée par le formulaire et on indique le nombre de dose*/
	        						while($donnees3 = $requete3->fetch()){
	        							echo "<option value=\"" . $donnees3['BouteilleID'] . "\">" . $donnees3['BouteilleName'] . "</option>";
	        						}
	        					?>
	        				</select>
	        				<label for="liquide3_dose"> Nombre de dose :</label>
	        				<input type="number" name="liquide3_dose" id="liquide3_dose" min="0" max="5" size="10" value="0" />
	        				
	        				<br />
	        				<br />

	        				<label for="liquide4">Quatrième liquide à verser : </label>
	        				<select name="liquide4" id="liquide4" />
	        					<?php
	        					/*On affiche toutes les bouteilles disponibles dans la base de données dans une liste déroulante et on récupère l'ID de la bouteille qui sera envoyée par le formulaire et on indique le nombre de dose*/
	        						while($donnees4 = $requete4->fetch()){
	        							echo "<option value=\"" . $donnees4['BouteilleID'] . "\">" . $donnees4['BouteilleName'] . "</option>";
	        						}
	        					?>
	        				</select>
	        				<label for="liquide4_dose"> Nombre de dose :</label>
	        				<input type="number" name="liquide4_dose" id="liquide4_dose" min="0" max="5" size="10" value="0" />
	        				
	        				<br />
	        				<br />

	        				<label for="liquide5">Cinquième liquide à verser : </label>
	        				<select name="liquide5" id="liquide5" />
	        					<?php
	        					/*On affiche toutes les bouteilles disponibles dans la base de données dans une liste déroulante et on récupère l'ID de la bouteille qui sera envoyée par le formulaire et on indique le nombre de dose*/
	        						while($donnees5 = $requete5->fetch()){
	        							echo "<option value=\"" . $donnees5['BouteilleID'] . "\">" . $donnees5['BouteilleName'] . "</option>";
	        						}
	        					?>
	        				</select>
	        				<label for="liquide5_dose"> Nombre de dose :</label>
	        				<input type="number" name="liquide5_dose" id="liquide5_dose" min="0" max="5" size="10" value="0" />
	        				
	        				<br />
	        				<br />

	        				<label for="liquide6">Sixième liquide à verser : </label>
	        				<select name="liquide6" id="liquide6" />
	        					<?php
	        					/*On affiche toutes les bouteilles disponibles dans la base de données dans une liste déroulante et on récupère l'ID de la bouteille qui sera envoyée par le formulaire et on indique le nombre de dose*/
	        						while($donnees6 = $requete6->fetch()){
	        							echo "<option value=\"" . $donnees6['BouteilleID'] . "\">" . $donnees6['BouteilleName'] . "</option>";
	        						}
	        					?>
	        				</select>
	        				<label for="liquide6_dose"> Nombre de dose :</label>
	        				<input type="number" name="liquide6_dose" id="liquide6_dose" min="0" max="5" size="10" value="0" />
	        				<br />
	        				<br />
	        				<br />
	        				<input type="submit" value="Valider" id="valider"><br />
	   					</p>
					</form>
				</div>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de validation des formulaires
			const elt = document.getElementById('valider');
			elt.addEventListener('click', function valider(event) {
				alert("Article ajouté.");
				document.location = "IHM_Liste_Articles.php";
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				document.location = "IHM_Liste_Articles.php";
			})
		</script>
	</body>
</html>
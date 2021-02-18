<?php
	/*Page permettant de saisir les nouvelles informations d'une boisson ou d'une bouteille déjà présente dans la base de données avec les formulaires appelant respectivement modif_boisson.php ou modif_bouteille.php*/
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Modifier un article</title>

		<!-- Fonctions qui permettent d'afficher le formulaire de modification d'une bouteille OU d'une boisson -->
		<script type="text/javascript">
			function aff_bouteille(action){
    			document.getElementById('block_bouteille').style.display = (action == "oui")? "inline" : "none";
			}
			function aff_boisson(action){
    			document.getElementById('block_boisson').style.display = (action == "oui")? "inline" : "none";
			}
		</script>
	</head>

	<body>
		<div id="bloc_page">
			<?php

				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");

				/*Création de la requète qui va récupérer les informations des bouteilles dans Bouteille_tb. On ne recupère pas l'ID = 0 ni l'ID = 1 car on ne doit pas les modifier*/
				$requete_bouteille = $bdd->query('SELECT * FROM Bouteille_tb WHERE BouteilleID <> 0 AND BouteilleID <> 1');

				/*Création de la requète qui va récupérer les informations des recettes dans Recette_tb*/
				$requete_recette = $bdd->query('SELECT RecetteID, RecetteName FROM Recette_tb');

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

				<!-- Permet de choisir entre une modification de boisson et une modification de bouteille grâce à l'appel des fonctions définies en début de page -->
				<div id="Choix_modif">
					<h3>Que voulez vous modifier ?</h3>
					<input type="radio" name="Choix_ajout" value="Bouteille" onchange="aff_bouteille('oui'); aff_boisson('non')" /><label class="label-radio">Une bouteille</label><br/>
		        	<input type="radio" name="Choix_ajout" value="Boisson" onchange="aff_bouteille('non'); aff_boisson('oui')" /><label class="label-radio">Une boisson</label><br/><br/>
				</div>

<!-- ------------------------------------------------------------ Modification d'une bouteille ------------------------------------------------------------ -->

				<div id="block_bouteille" hidden="hidden">
					<h3>Sélectionner la bouteille à modifier</h3>
					<!-- Formulaire qui permet de modifier les informations d'une bouteille -->
					<form method="post" action="modif_bouteille.php">
						<select name="bouteille_modifiee" id="bouteille_modifiee">
						<?php
						/*On récupère les informations depuis requete_bouteille et on les affiches dans une liste déroulante. Chaque bouteille va créer une option dans la liste. Cette liste permet de choisir la bouteille qui sera modifiée grâce à son ID*/
							while($bouteilles = $requete_bouteille->fetch()){
								echo "<option value=\"" . $bouteilles['BouteilleID'] . "\">" . $bouteilles['BouteilleName'] . "</option>";
	        				}
						?>
					</select>

					<h3>Saisir les nouvelles informations</h3>

	    			<p>
	    				<!-- Saisie des nouvelles informations de la bouteille -->
	        			<label for="nom_bouteille">Nom de la bouteille :</label>
	        			<input type="text" name="nom_bouteille" id="nom_bouteille" size="30" maxlength="30" />
	        			<br />
	        			<br />
	        			<label for="doseur">Doseur associé :</label>
	        			<select name="doseur" id="doseur">
	        				<option value="25">25 mL</option>
	        				<option value="35">35 mL</option>
	        				<option value="50">50 mL</option>
	        			</select>
	        			<br />
	        			<br />
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
	   				</p>
	   				<br />
	   				<input type="submit" name="modif_bouteille_ok" value="Modifier" id="modif_bouteille" />
	   				<br />
					</form>
				</div>


<!-- ------------------------------------------------------------ Modification d'une boisson ------------------------------------------------------------ -->


				<div id="block_boisson" hidden="hidden">
					<h3>Sélectionner la boisson à modifier</h3>
					<!-- Formulaire qui permet de modifier les informations d'une boisson -->
					<form method="post" action="modif_boisson.php">
					<select name="modif_boisson" id="modif_boisson">
						<?php
						/*On récupère les informations depuis requete_recette et on les affiches dans une liste déroulante. Chaque recette va créer une option dans la liste. Cette liste permet de choisir la recette qui sera modifiée grâce à son ID*/
							while($articles = $requete_recette->fetch()){
								echo "<option value=\"" . $articles['RecetteID'] . "\">" . $articles['RecetteName'] . "</option>";
							}
						?>
					</select>

					<h3>Saisir les nouvelles informations</h3>
				
	    				<p>
	    					<!-- Saisie des nouvelles informations de la boisson -->
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
	        				<input type="submit" name="modif_boisson_ok" value="Modifier" id="modif_boisson_ok" />
	        				<br />
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
			//Bouton de validation de modification d'une bouteille
			const elt_bouteille = document.getElementById('modif_bouteille');
			elt_bouteille.addEventListener('click', function modifier_bouteille(event) {
				if(confirm("Appliquer les modifications ?")){
					alert("La bouteille a été modifiée.")
					document.location = "IHM_Liste_Articles.php";
				}
				else{

				}
			})

			//Bouton de validation de modification d'une boisson
			const elt_boisson = document.getElementById('modif_boisson_ok');
			elt_boisson.addEventListener('click', function modifier_boisson(event) {
				if(confirm("Appliquer les modifications ?")){
					alert("La boisson a été modifiée.")
					document.location = "IHM_Liste_Articles.php";
				}
				else{

				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				document.location = "IHM_Liste_Articles.php";
			})
		</script>
	</body>
</html>
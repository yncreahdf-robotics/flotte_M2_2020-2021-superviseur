<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Liste des articles</title>
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
				
				include("connexion.php");

				$requete_recette = $bdd->query('
					SELECT r.RecetteName AS RecetteName, 
						   a.ArticlePrice AS ArticlePrice, a.ArticleWeight AS ArticleWeight, 
						   b.BouteilleName AS 1stBouteilleName, b.VolumeDoseur AS 1stVolumeDoseur, r.Quantity1,
						   b2.BouteilleName AS 2ndBouteilleName, b2.VolumeDoseur AS 2ndVolumeDoseur, r.Quantity2,
						   b3.BouteilleName AS 3rdBouteilleName, b3.VolumeDoseur AS 3rdVolumeDoseur, r.Quantity3,
						   b4.BouteilleName AS 4thBouteilleName, b4.VolumeDoseur AS 4thVolumeDoseur, r.Quantity4,
						   b5.BouteilleName AS 5thBouteilleName, b5.VolumeDoseur AS 5thVolumeDoseur, r.Quantity5,
						   b6.BouteilleName AS 6thBouteilleName, b6.VolumeDoseur AS 6thVolumeDoseur, r.Quantity6
					FROM Recette_tb r
					INNER JOIN Article_tb a ON a.IDRecette = r.RecetteID
					INNER JOIN Bouteille_tb b ON b.BouteilleID = r.BouteilleID1
					INNER JOIN Bouteille_tb b2 ON b2.BouteilleID = r.BouteilleID2
					INNER JOIN Bouteille_tb b3 ON b3.BouteilleID = r.BouteilleID3
					INNER JOIN Bouteille_tb b4 ON b4.BouteilleID = r.BouteilleID4
					INNER JOIN Bouteille_tb b5 ON b5.BouteilleID = r.BouteilleID5
					INNER JOIN Bouteille_tb b6 ON b6.BouteilleID = r.BouteilleID6
					');
				$requete_bouteille = $bdd->query('SELECT * FROM Bouteille_tb'); //Lecture table Bouteille depuis la bdd
			?>
			
			<?php include("entete.php"); ?>
		
			<section>
				
				<div id="Listes">
					<div id="Tableau">
						<div id="block_boisson">
							<h2>Liste des Articles</h2>
							<table>
								<thead>
									<tr>
										<th>Nom</th>
										<th>Prix (€)</th>
										<th>Quantité (cL)</th>
										<th>Recette</th>
									</tr>
								</thead>

								<tfoot>
									<tr>
										<th>Nom</th>
										<th>Prix (€)</th>
										<th>Quantité (cL)</th>
										<th>Recette</th>
									</tr>
								</tfoot>

								<tbody>
									<?php
										while($donnees = $requete_recette->fetch()){
									?>
									<tr>
										<td><?php echo $donnees['RecetteName'] ;?></td>
										<td><?php echo $donnees['ArticlePrice'] ;?></td>
										<td><?php echo $donnees['ArticleWeight'] ;?></td>
										<td><?php 
											if($donnees['1stBouteilleName'] != 'Pas de bouteille'){
												echo $donnees['1stBouteilleName'] . " (" . $donnees['1stVolumeDoseur'] . " mL * " . $donnees['Quantity1'] . ")" ;
											}
											if($donnees['2ndBouteilleName'] != 'Pas de bouteille'){
												echo " - " . $donnees['2ndBouteilleName'] . " (" . $donnees['2ndVolumeDoseur'] . " mL * " . $donnees['Quantity2'] . ")" ;
											}

											if($donnees['3rdBouteilleName'] != 'Pas de bouteille'){
												echo "<br /> - " . $donnees['3rdBouteilleName'] . " (" . $donnees['3rdVolumeDoseur'] . " mL * " . $donnees['Quantity3'] . ")" ;
											}

											if($donnees['4thBouteilleName'] != 'Pas de bouteille'){
												echo " - " . $donnees['4thBouteilleName'] . " (" . $donnees['4thVolumeDoseur'] . " mL * " . $donnees['Quantity4'] . ")" ;
											}

											if($donnees['5thBouteilleName'] != 'Pas de bouteille'){
												echo "<br /> - " . $donnees['5thBouteilleName'] . " (" . $donnees['5thVolumeDoseur'] . " mL * " . $donnees['Quantity5'] . ")" ;
											}

											if($donnees['6thBouteilleName'] != 'Pas de bouteille'){
												echo " - " . $donnees['6thBouteilleName'] . " (" . $donnees['6thVolumeDoseur'] . " mL * " . $donnees['Quantity6'] . ")" ;
											}
										?></td>
									</tr>
									<?php
										}
									?>
								</tbody>
							</table>
						</div>

						<div id="block_bouteille" hidden="hidden">
							<h2>Liste des Bouteilles</h2>
							<table>
								<thead>
									<tr>
										<th>Nom</th>
										<th>Doseur associé (mL)</th>
										<th>Emplacement actuel</th>
									</tr>
								</thead>

								<tfoot>
									<tr>
										<th>Nom</th>
										<th>Doseur associé (mL)</th>
										<th>Emplacement actuel</th>
									</tr>
								</tfoot>

								<tbody>
									<?php
										while($bouteille = $requete_bouteille->fetch()){
									?>
									<tr>
										<td><?php echo $bouteille['BouteilleName'] ;?></td>
										<td><?php echo $bouteille['VolumeDoseur'] ;?></td>
										<td><?php echo $bouteille['Emplacement'] ;?></td>
									</tr>
									<?php
										}
									?>
								</tbody>
							</table>
						</div>
					</div>
					<br />
					<div id="affichage">
						<input type="radio" name="choix_affichage" id="article" checked="checked" onchange="aff_boisson('oui'); aff_bouteille('non')" /><label for="article">Afficher les articles</label>
						<input type="radio" name="choix_affichage" id="bouteille" onchange="aff_boisson('non'); aff_bouteille('oui')" /><label for="bouteille">Afficher les bouteilles</label>
					</div>
					<nav>
						<div class="bouton" id="ajouter">
							<a href="IHM_Ajouter_Article.php">Ajouter un article</a>
						</div>
						<div class="bouton" id="modifier">
							<a href="IHM_Modifier_Article.php">Modifier un article</a>
						</div>
						<div class="bouton" id="supprimer">
							<a href="IHM_Supprimer_Article.php">Supprimer un article</a>
						</div>
					</nav>
				</div>
			</section>

			<?php include("pied_de_page.php"); ?>

		</div>
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Page_Proprietaire.php";
			})

			//Bouton pour ajouter un article
			const elt_ajouter = document.getElementById('ajouter');
			elt_ajouter.addEventListener('click', function ajouter(event){
				event.preventDefault()
				document.location = "IHM_Ajouter_Article.php";
			})

			//Bouton pour modifier un article
			const elt_modifier = document.getElementById('modifier');
			elt_modifier.addEventListener('click', function modifer(event){
				event.preventDefault()
				document.location = "IHM_Modifier_Article.php";
			})

			//Bouton pour supprimer un article
			const elt_supprimer = document.getElementById('supprimer');
			elt_supprimer.addEventListener('click', function supprimer(event){
				event.preventDefault()
				document.location = "IHM_Supprimer_Article.php";
			})
		</script>
	</body>
</html>
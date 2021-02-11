<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Suivi des robots</title>
	</head>

	<body>

		<?php
			
			/*Connexion à la base de données avec le fichier connexion.php*/
			include("connexion.php");
			
			/*Création de la requète qui va récupérer les informations des tables dans Table_tb*/
			$requete = $bdd->query('
				SELECT TableID, Etat 
				FROM Table_tb
			');

			/*Création de la requète qui va récupérer les informations des bouteilles présentent sur le tourniquet dans la table Bouteille_tb. La requète fait le tri en regardant si l'emplacement de la bouteille est égale à 0. Les bouteilles sont classées par ordre d'emplacement*/
			$requete_bouteille = $bdd->query('
				SELECT BouteilleName, Emplacement 
				FROM Bouteille_tb 
				WHERE Emplacement <> 0 	/* <> équivaut à != */
				ORDER BY Emplacement
			')  
		?>

		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<nav id="Suivi_Salle">
					<!-- Affichage de la carte de la salle -->
					<div id="map">
						<h3>Position en temps réel des robots dans la salle</h3>
						<img src="images/Map_Robot.png" alt="Map des robots dans la salle" id="map_robot" />
					</div>
					<div class="Tableau" id="bouteille">
						
						<h3>Bouteille en place sur le tourniquet</h3>
						<!-- Création du tableau des bouteilles du tourniquet -->
						<table>
							<thead>
								<tr>
									<th>Emplacement</th>
									<th>Bouteille</th>
								</tr>
							</thead>

							<tfoot>
								<tr>
									<th>Emplacement</th>
									<th>Bouteille</th>
								</tr>
							</tfoot>
							<tbody>
								<?php
								/*On récupère les informations depuis requete_bouteille et on les affiches dans un tableau de 6 lignes. On regarde si une bouteille est à chaque emplacement, et on l'affiche si c'est le cas, sinon on affiche une ligne sans bouteille*/
									if($requete_bouteille->rowCount() > 0){
										$bouteille = $requete_bouteille->fetch();
										$lignes_restantes = 6;
										for($nombre_de_lignes = 1; $nombre_de_lignes <= $requete_bouteille->rowCount(); $nombre_de_lignes++){
											if($bouteille['Emplacement'] == $nombre_de_lignes){
								?>
												<tr>
													<td><?php echo $nombre_de_lignes ;?></td>
													<td><?php echo $bouteille['BouteilleName'] ;?></td>
												</tr>
								<?php
												$bouteille= $requete_bouteille->fetch();
											}
											else{
								?>
												<tr>
													<td><?php echo $nombre_de_lignes ;?></td>
													<td>Pas de bouteille</td>
												</tr>
								<?php
											$lignes_restantes--;
											}

										}
										for($nombre_de_lignes_restantes = $nombre_de_lignes; $nombre_de_lignes_restantes <= $lignes_restantes; $nombre_de_lignes_restantes++){
								?>
												<tr>
													<td><?php echo $nombre_de_lignes_restantes ;?></td>
													<td>Pas de bouteille</td>
												</tr>
								<?php
										}
									}
									else{
								?>
									<tr>
										<td>1</td>
										<td>Pas de bouteille</td>
									</tr>
									<tr>
										<td>2</td>
										<td>Pas de bouteille</td>
									</tr>
									<tr>
										<td>3</td>
										<td>Pas de bouteille</td>
									</tr>
									<tr>
										<td>4</td>
										<td>Pas de bouteille</td>
									</tr>
									<tr>
										<td>5</td>
										<td>Pas de bouteille</td>
									</tr>
									<tr>
										<td>6</td>
										<td>Pas de bouteille</td>
									</tr>
								<?php
									}
								?>

							</tbody>
						</table>
						<!-- Création d'un bouton qui permet d'accéder à un outil pour indiquer un déplacement de bouteille sur le tourniquet -->
						<div class="bouton" id="tourniquet">
							<p>Déplacer une bouteille</p>
						</div>
					</div>

					<div class="Tableau" id="table">
						<h3>Liste et état des tables de la salle</h3>
						<!-- Création du tableau des tables de la salle -->
						<table>
							<thead>
								<tr>
									<th>Table</th>
									<th>Etat</th>
									<th></th>
								</tr>
							</thead>

							<tfoot>
								<tr>
									<th>Table</th>
									<th>Etat</th>
									<th></th>
								</tr>
							</tfoot>

							<tbody>
								<?php 
								/*On récupère les informations depuis requete et on les affiches dans un tableau de taille variable. Chaque table va créer une ligne du tableau. On ajoute un bouton pour libérer chaque tables lorsqu'un client quitte la table*/
									while($donnees = $requete->fetch()){
								?>
								<tr>
									<td><?php echo $donnees['TableID']; ?></td>
									<td><?php echo $donnees['Etat']; ?></td>
									<td><?php echo "<input type=\"submit\" value=\"Libérer la table\" id=\"table".$donnees['TableID']."\"/>" ;?></td>
								</tr>
								<?php
									}
								?>
							</tbody>
						</table>
					</div>
				</nav>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			const elt_table1 = document.getElementById('table1');
			elt_table1.addEventListener('click', function table1(event) {
				//Lien BDD pour changer l'état de la table sélectionnée vers "Libre"
				<?php
					$bdd->exec('UPDATE Table_tb SET Etat = \'FREE\' WHERE TableID = 1');
					?>
			})

			const elt_table2 = document.getElementById('table2');
			elt_table2.addEventListener('click', function table1(event) {
				//Lien BDD pour changer l'état de la table sélectionnée vers "Libre"
				<?php
					$bdd->exec('UPDATE Table_tb SET Etat = \'FREE\' WHERE TableID = 2');
					?>
			})

			const elt_table3 = document.getElementById('table3');
			elt_table3.addEventListener('click', function table1(event) {
				//Lien BDD pour changer l'état de la table sélectionnée vers "Libre"
				<?php
					$bdd->exec('UPDATE Table_tb SET Etat = \'FREE\' WHERE TableID = 3');
					?>
			})

			//Bouton de déplacement des bouteilles
			const elt_tourniquet = document.getElementById('tourniquet');
			elt_tourniquet.addEventListener('click', function tourniquet(event){
				//event.preventDefault()
				document.location = "IHM_Deplacer_Bouteille.php";
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				//event.preventDefault()
				document.location = "IHM_Page_Proprietaire.php";
			})
		</script>
	</body>
</html>
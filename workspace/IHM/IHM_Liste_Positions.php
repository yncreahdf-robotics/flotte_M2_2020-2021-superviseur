<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Liste des positions</title>
	</head>

	<body>
		<div id="bloc_page">
			<?php
				
				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");


				/*Création de la requète qui va récupérer les positions dans Pose_tb*/
				$requete = $bdd->query('SELECT * FROM Pose_tb');	
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Liste des Positions</h2>
				<div id="Listes">
					<div class="Tableau">
						<!-- Création du tableau des positions -->
						<table>
							<thead>
								<tr>
									<th>Nom</th>
									<th>Position X</th>
									<th>Position Y</th>
									<th>Position Z</th>
									<th>Angle ω</th>
								</tr>
							</thead>

							<tfoot>
								<tr>
									<th>Nom</th>
									<th>Position X</th>
									<th>Position Y</th>
									<th>Position Z</th>
									<th>Angle ω</th>
								</tr>
							</tfoot>

							<tbody>
								<?php
								/*On récupère les informations depuis requete et on les affiches dans un tableau de taille variable. Chaque recette va créer une nouvelle ligne du tableau*/
									while($donnees = $requete->fetch()){
								?>
								<tr>
									<td><?php echo $donnees['PoseName'] ;?></td>
									<td><?php echo $donnees['PoseX'] ;?></td>
									<td><?php echo $donnees['PoseY'] ;?></td>
									<td><?php echo $donnees['PoseZ'] ;?></td>
									<td><?php echo $donnees['PoseW'] ;?></td>
								</tr>
								<?php
									}
								?>
							</tbody>
						</table>
					</div>

					<!-- Créations de différents boutons permettant d'accéder aux outils de gestions des bouteilles ou des boissons -->
					<nav>
						<div class="bouton" id="ajouter">
							<p>Ajouter une position</p>
						</div>
						<div class="bouton" id="modifier">
							<p>Modifier une position</p>
						</div>
						<div class="bouton" id="supprimer">
							<p>Supprimer une position</p>
						</div>
					</nav>
				</div>
			</section>

			<!-- Affichage du pied de page avecle fichier pied_de_page.php -->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				//event.preventDefault()
				document.location = "IHM_Page_Proprietaire.php";
			})

			//Bouton pour ajouter une position
			const elt_ajouter = document.getElementById('ajouter');
			elt_ajouter.addEventListener('click', function ajouter(event){
				//event.preventDefault()
				document.location = "IHM_Ajouter_Position.php";
			})

			//Bouton pour modifier une position
			const elt_modifier = document.getElementById('modifier');
			elt_modifier.addEventListener('click', function modifer(event){
				//event.preventDefault()
				document.location = "IHM_Modifier_Position.php";
			})

			//Bouton pour supprimer une position
			const elt_supprimer = document.getElementById('supprimer');
			elt_supprimer.addEventListener('click', function supprimer(event){
				//event.preventDefault()
				document.location = "IHM_Supprimer_Position.php";
			})
		</script>
	</body>
</html>
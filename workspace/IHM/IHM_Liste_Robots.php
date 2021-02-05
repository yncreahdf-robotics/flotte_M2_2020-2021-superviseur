<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Liste des robots</title>
	</head>

	<body>
		<div id="bloc_page">
			<?php
				
				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");

				/*Création de la requète qui va récupérer les informations des robots dans Robot_tb*/
				$requete = $bdd->query('
					SELECT RobotIP, RobotType, Position, Etat 
					FROM Robot_tb
				');
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Liste des robots</h2>
				<div id="Listes">
					<div id="Tableau">
						<!-- Création du tableau des robots -->
						<table>
							<thead>
								<tr>
									<th>ID Robot</th>
									<th>Type de Robot</th>
									<th>Disponibilité</th>
									<th>Dernière position</th>
								</tr>
							</thead>

							<tfoot>
								<tr>
									<th>ID Robot</th>
									<th>Type de Robot</th>
									<th>Disponibilité</th>
									<th>Dernière position</th>
								</tr>
							</tfoot>

							<tbody>
								<?php
								/*On récupère les informations depuis requete et on les affiches dans un tableau de taille variable. Chaque recette va créer une nouvelle ligne du tableau*/
									while($donnees = $requete->fetch()){
								?>
								<tr>
									<td><?php echo $donnees['RobotIP'] ;?></td>
									<td><?php echo $donnees['RobotType'] ;?></td>
									<td><?php echo $donnees['Etat'] ;?></td>
									<td><?php echo $donnees['Position'] ;?></td>
								</tr>
								<?php
									}
								?>
							</tbody>
						</table>
					</div>

					<!-- Création d'un bouton permettant d'accéder à un outil d'ajout de type de robot -->
					<nav>
						<div class="bouton" id="ajout_robot">
							<p>Ajouter un type de robot<p>
						</div>
					</nav>
				</div>
			</section>

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

			//Bouton ajout robot
			const elt_ajout = document.getElementById('ajout_robot');
			elt_ajout.addEventListener('click', function ajout_robot(event){
				//event.preventDefault()
				document.location = "IHM_Ajouter_Robot.php";
			})
		</script>
	</body>
</html>
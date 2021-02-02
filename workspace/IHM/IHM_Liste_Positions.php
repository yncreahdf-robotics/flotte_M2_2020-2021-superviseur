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
				
				include("connexion.php");

				$requete = $bdd->query('SELECT * FROM Pose_tb');	//Lecture table Pose depuis la bdd
			?>
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Liste des Positions</h2>
				<div id="Listes">
					<div id="Tableau">
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
					<nav>
						<div class="bouton" id="ajouter">
							<a href="IHM_Ajouter_Position.php">Ajouter une position</a>
						</div>
						<div class="bouton" id="modifier">
							<a href="IHM_Modifier_Position.php">Modifier une position</a>
						</div>
						<div class="bouton" id="supprimer">
							<a href="IHM_Supprimer_Position.php">Supprimer une position</a>
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
				document.location = "IHM_Ajouter_Position.php";
			})

			//Bouton pour modifier un article
			const elt_modifier = document.getElementById('modifier');
			elt_modifier.addEventListener('click', function modifer(event){
				event.preventDefault()
				document.location = "IHM_Modifier_Position.php";
			})

			//Bouton pour supprimer un article
			const elt_supprimer = document.getElementById('supprimer');
			elt_supprimer.addEventListener('click', function supprimer(event){
				event.preventDefault()
				document.location = "IHM_Supprimer_Position.php";
			})
		</script>
	</body>
</html>
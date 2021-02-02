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
				try{
					$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
				}
				catch(Exception $e){
					die('Erreur : '.$e->getMessage());
				}
				$requete = $bdd->query('SELECT RobotIP, RobotType, Position, Etat FROM Robot_tb');	//Lecture table Robot depuis la bdd
			?>
			
			<?php include("entete.php"); ?>
		
			<section>
				<h2>Liste des robots</h2>
				<div id="Listes">
					<div id="Tableau">
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
					<nav>
						<div class="bouton" id="ajout_robot">
							<a href="IHM_Ajouter_Robot.php">Ajouter un type de robot</a>
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

			//Bouton ajout robot
			const elt_ajout = document.getElementById('ajout_robot');
			elt_ajout.addEventListener('click', function ajout_robot(event){
				event.preventDefault()
				document.location = "IHM_Ajouter_Robot.php";
			})
		</script>
	</body>
</html>
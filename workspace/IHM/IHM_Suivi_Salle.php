<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Suivi des robots</title>
	</head>

	<body>

		<?php
			try{
				$bdd = new PDO('mysql:host=172.19.0.3;dbname=flotte_db', 'root', 'root', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
			}
			catch(Exception $e){
				die('Erreur : '.$e->getMessage());
			}
			$requete = $bdd->query('SELECT TableID, Etat FROM Table_tb');	//Lecture de la base de donnée
		?>

		<div id="bloc_page">
			
			<?php include("entete.php"); ?>
		
			<section>
				<nav id="Suivi_Salle">
					<div id="map">
						<h3>Position en temps réel des robots dans la salle</h3>
						<img src="images/Map_Robot.png" alt="Map des robots dans la salle" id="map_robot" />
					</div>
					<div id="Tableau">
						<h3>Liste et état des tables de la salle</h3>
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

			<?php include("pied_de_page.php"); ?>

		</div>
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


			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function retour(event){
				event.preventDefault()
				document.location = "IHM_Page_Proprietaire.php";
			})
		</script>
	</body>
</html>
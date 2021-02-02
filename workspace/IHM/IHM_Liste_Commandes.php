<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Liste des commandes</title>
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
			$requete = $bdd->query('SELECT a.ArticleName, c.CommandNbr, c.Etat
				FROM Commande_tb c			/*Lecture tables Article et Commande depuis la bdd*/
				INNER JOIN Article_tb a 	/*On fait la jointure entre les 2 bdd*/
				ON c.ArticleID = a.ArticleID');
			?>
			
			<?php include("entete.php"); ?>

			<section>
				<h2>Liste des commandes</h2>
				<div id="Tableau">
					<table>
						<thead>
							<tr>
								<th>N° Commande</th>
								<th>Article Commandé</th>
								<th>Etat</th>
							</tr>
						</thead>

						<tfoot>
							<tr>
								<th>N° Commande</th>
								<th>Article Commandé</th>
								<th>Etat</th>
							</tr>
						</tfoot>

						<tbody>
							<?php
									while($donnees = $requete->fetch()){
								?>
							<tr>
								<td><?php echo $donnees['CommandNbr'] ;?></td>
								<td><?php echo $donnees['ArticleName'] ;?></td>
								<td><?php echo $donnees['Etat'] ;?></td>
							</tr>
							<?php
								}
							?>
						</tbody>
					</table>
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
		</script>
	</body>
</html>
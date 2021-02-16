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
				
				/*Connexion à la base de données avec le fichier connexion.php*/
				include("connexion.php");

				/*Création de la requète qui va récupérer les commandes dans Commande_tb avec les articles associés grâce au "INNER JOIN"*/
				$requete = $bdd->query('SELECT a.ArticleName, c.CommandNbr, c.Etat
					FROM Commande_tb c			
					INNER JOIN Article_tb a 	/*On fait la jointure entre les 2 bdd*/
					ON c.ArticleID = a.ArticleID');
			?>
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>

			<section>
				<h2>Liste des commandes</h2>
				<div class="Tableau">
					<!-- Création du tableau des commandes -->
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
							/*On récupère les informations depuis requete et on les affiches dans un tableau de taille variable. Chaque recette va créer une nouvelle ligne du tableau*/
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
				<br />
				<br />
				<form method="post" action="supprimer_commande.php">
					<p>
						<label for="supprimer_commande">Indiquer le numéro de commande à supprimer : </label>
						<input type="number" name="commande_supprimee" id="commande_supprimee" size="10" />
						<input type="submit" name="supprimer" value="Supprimer" id="supprimer" />
					</p>
				</form>
			</section>

			<!-- Affichage du pied de page avec le fichier pied_de_page.php -->
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
		</script>
	</body>
</html>
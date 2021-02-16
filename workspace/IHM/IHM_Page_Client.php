<?php 
	session_start();	//On démarre une session pour utiliser un panier associé au client

	include_once("fonctions_panier.php");


	creationPanier();
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="IHM.css" />
		<title>Accueil Client</title>
	</head>

	<body>
		<?php
			
			/*Connexion à la base de données avec le fichier connexion.php*/
			include("connexion.php");


			/*Création de la requète qui va récupérer les informations des articles dans Article_tb*/
			$requete_article = $bdd->query('
				SELECT ArticleID, ArticleName, ArticlePrice, ArticleWeight 
				FROM Article_tb
			');	

			/*Création de la requète qui va récupérer les tables dans la base de données*/
			$requete_table = $bdd->query('
				SELECT TableID
				FROM Table_tb
			');
		?>

		<div id="bloc_page">
			
			<!-- Affichage de l'entete de la page avec le fichier entete.php -->
			<?php include("entete.php"); ?>
		
			<section>

				<h2>Liste des articles :</h2>

				<form action="panier_client.php" method="post">
                    <!-- Formulaire qui permet au client de saisir les articles qu'il veut commander et d'indiquer la table à laquelle il est installé-->
                    <h3>Indiquez la table à laquelle vous êtes installé</h3>
                    <select name="table" id="table">
                    	<?php
                    	/*Affichage des tables de la salle dans une liste déroulante*/
                    		while($table = $requete_table->fetch()){
                    			echo "<option value=\"" . $table['TableID'] . "\">Table " . $table['TableID'] . "</option>";
                    		}
                    	?>
                    </select>
                    <h3>Choisissez la boisson que vous voulez ajouter à votre commande ainsi que sa quantité</h3>

                    <select name="article_commande" id="article_commande">
                    	<?php
                    	/*Affichage des articles dans une liste déroulante*/
                    		while($articles = $requete_article->fetch()){
								echo "<option value=\"" . $articles['ArticleID'] . "\">" . $articles['ArticleName'] . " - " . $articles['ArticleWeight'] . " cL - " . $articles['ArticlePrice'] . "€</option>";
							}
                    	?>
                    </select>

                    <input type="number" name="quantite_article" id="quantite_article" min="1" step="1"  value="1" size="5" />

                    <br />
                    <br />

					<input type="submit" name="ajouter_panier" value="Ajouter" id="ajout_panier" />
				</form>
				
				<br />

				<!-- Création de boutons permettant de pré-valider la commande ou d'appeler un serveur -->
				<nav>
					<div class="bouton" id="commande">
						<p>Commander</p>
					</div>
					<div class="bouton" id="appel_serveur">
						<p>Appeler un serveur</p>
					</div>
				</nav>
			</section>


			<!-- Affichage du pied de page avec le fichier pied_de_page.php-->
			<?php include("pied_de_page.php"); ?>

		</div>

		<!-- Fonctions qui permettent de gérer les boutons présents sur la page -->
		<script src="//code.jquery.com/jquery-1.12.0.min.js"></script>
		<script type="text/javascript">
			//Bouton pour pré-valider la commande
			const elt_commande = document.getElementById('commande');
			elt_commande.addEventListener('click', function commande(event){
				//event.preventDefault()
				document.location = "IHM_Commande_Client.php";
			})


			//Appel d'un serveur
			const elt_serveur = document.getElementById('appel_serveur');
			elt_serveur.addEventListener('click', function appel_serveur(event) {
				//event.preventDefault()
				if(confirm("Etes-vous sur de vouloir appeler un serveur ?")){
					alert("Un serveur a été appelé.")
				}
				else{
					
				}
			})

			//Bouton de retour
			const elt_retour = document.getElementById('Retour');
			elt_retour.addEventListener('click', function client(event){
				//event.preventDefault()
				document.location = "index.php";
			})
		</script>
	</body>
</html>

